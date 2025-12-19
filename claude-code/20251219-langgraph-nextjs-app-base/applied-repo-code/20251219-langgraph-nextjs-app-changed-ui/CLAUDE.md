# CLAUDE.md

このファイルは、Claude Code (claude.ai/code) がこのリポジトリで作業する際のガイダンスを提供します。

## プロジェクト概要

Next.js 15フロントエンドとFastAPIバックエンドを備えたLangGraph駆動のマルチエージェントチャットアプリケーション。システムはインテリジェントルーティングを使用してWeb検索が必要かどうかを判断し、複数の専門エージェントを調整してリサーチ、分析、包括的な回答の作成を行います。

## **注意事項**

コンテナベースで開発して欲しいので、コマンド実行する際などは、コンテナ内でやること。
開発したコードを最新で反映させたい時は、`make down-dev && make serve-dev`コマンドを実行して、コンテナを再起動＆ビルドしてください。

また、開発が完了したら、必ずフロントエンド、バックエンド両方のビルドテストを実行して、すべてが正常に動作することを確認してください。

## 必須コマンド

### 開発環境（ホットリロード有効）
```bash
make serve-dev     # 開発環境を起動
make logs-dev      # ログを表示（フォローモード）
make restart-dev   # コンテナを再起動
make down-dev      # 開発環境を停止
```

### 本番環境
```bash
make serve-prod    # 本番環境を起動
make down-prod     # 本番環境を停止
```

### その他のコマンド
```bash
make help          # 利用可能なすべてのコマンドを表示
make clean         # すべてのコンテナとボリュームを削除
make status        # コンテナの状態を確認
```

### アクセスURL
- フロントエンド: http://localhost:3000
- バックエンドAPI: http://localhost:8002
- APIドキュメント: http://localhost:8002/docs

### 環境変数
`.env`ファイルに必要な設定:
- `OPENAI_API_KEY` - OpenAI APIキー
- `OPENAI_MODEL` - モデル名（例: gpt-4.1-mini, gpt-5）
- `PERPLEXITY_API_KEY` - Web検索用Perplexity APIキー

## アーキテクチャ概要

### LangGraphエージェントワークフロー

コアアーキテクチャは、条件付きルーティングを備えたLangGraphのStateGraphを使用しています:

1. **Router Agent（ルーター）** (`backend/app/agents/router.py`)
   - すべてのクエリのエントリーポイント
   - ユーザーの質問と会話コンテキストを分析
   - リアルタイムWeb検索が必要かどうかを判断
   - ステートに`needs_research`フラグを設定
   - 時間に敏感な質問のために現在のJST日時を使用

2. **条件付きルーティング** (`backend/app/agents/graph.py:9-14`)
   - `needs_research=True`の場合: Router → Researcher → Analyzer → Composer
   - `needs_research=False`の場合: Router → Composer（直接パス）
   - この最適化により、一般的な知識に関する質問では不要なAPI呼び出しをスキップ

3. **Researcher Agent（リサーチャー）** (`backend/app/agents/researcher.py`)
   - Web検索が必要な場合のみ呼び出される
   - Perplexity APIを使用（`backend/app/services/perplexity.py`）
   - モデル「sonar-pro」で検索を実行
   - 引用付きの検索結果を返す

4. **Analyzer Agent（アナライザー）** (`backend/app/agents/analyzer.py`)
   - Researcherの後にのみ実行
   - 検索結果から洞察を抽出
   - パターンと重要な情報を特定

5. **Composer Agent（コンポーザー）** (`backend/app/agents/composer.py`)
   - すべてのパスの最終ステップ
   - ユーザーフレンドリーな回答を生成
   - 一貫性のある複数ターンの会話のために会話コンテキストを使用

### ステート管理

**AgentState** (`backend/app/agents/state.py`) は全エージェント間で共有されるTypedDictです:
- `user_query`: 現在のユーザーの質問
- `conversation_history`: コンテキスト用の過去のメッセージリスト
- `needs_research`: Routerによって設定されるブール値フラグ
- `messages`: LangGraphメッセージ履歴（`add_messages`リデューサーを使用）
- `research_data`: Researcherからの生の検索結果
- `analysis_result`: Analyzerからの処理済み洞察
- `final_answer`: Composerからの最終回答
- `step_history`: フロントエンド可視化用のエージェントアクションリスト

### APIエンドポイント

**バックエンド** (`backend/app/api/chat.py`):
- `POST /api/chat` - メインチャットエンドポイント、エージェントグラフを実行
- `GET /api/workflow/graph` - LangGraphのPNG可視化を返す
- `GET /api/workflow/info` - エージェントメタデータと説明を返す
- `GET /health` - ヘルスチェック

**フロントエンド** (`frontend/app/page.tsx`):
- `/` にシングルページアプリ
- `ChatInterface` コンポーネントがユーザー入出力を処理
- `WorkflowViewer` コンポーネントがエージェントワークフローの可視化を表示

### Docker アーキテクチャ

3つのDocker Compose構成:
- `docker-compose.yaml` - 基本構成（レガシー）
- `docker-compose.dev.yaml` - ボリュームマウントとホットリロード付き開発環境
- `docker-compose.prod.yaml` - 最適化されたビルドの本番環境

**開発モード** (dev):
- フロントエンド: Next.js Fast Refreshを使用した`npm run dev`
- バックエンド: watchfilesを使用した`uvicorn --reload`
- すべてのソースディレクトリがボリュームとしてマウント
- 変更は1〜3秒で反映

**本番モード** (prod):
- フロントエンド: パフォーマンス最適化のためのNext.js standaloneビルド
- バックエンド: リロードなしの標準uvicorn
- ボリュームマウントなし

## 重要な実装の詳細

### エージェントグラフの構築
グラフはモジュールインポート時に一度だけコンパイルされ（`backend/app/api/chat.py:10`）、すべてのリクエストで再利用されます。これにより、各API呼び出しでLangGraphワークフローを再作成することを回避します。

### 非同期実行
すべてのエージェントは`async def execute()`メソッドを使用し、グラフは`await agent_graph.ainvoke()`で呼び出され、API呼び出し中のノンブロッキングI/Oを実現します。

### エラーハンドリング
- Perplexity APIの失敗は`{"success": False, "error": ..., "content": "Web search failed"}`を返す
- チャットエンドポイントはグラフ実行をtry/exceptでラップし、エラー時には詳細付きのHTTP 500を返す

### フロントエンド-バックエンド通信
フロントエンドはDockerネットワーク内で`NEXT_PUBLIC_API_URL=http://backend:8000`を使用します。バックエンドのCORSミドルウェアは`localhost:3000`と`frontend:3000`の両方を許可します。

### 会話コンテキスト
Routerエージェントは`conversation_history`から最後の5メッセージのみを使用し（`router.py:54`）、最近のコンテキストを維持しながらプロンプトを簡潔に保ちます。

### モデル設定
Routerエージェントは`temperature=1.0`を使用します（`router.py:15`）。これはgpt-4.1-miniモデルで必要です。他のエージェントはニーズに応じて異なる温度を使用できます。

## 開発ワークフロー

1. **開発モードでコード変更が自動検出される**
   - フロントエンド: `app/`、`components/`、`lib/`の変更がFast Refreshをトリガー
   - バックエンド: `app/`の変更がuvicornリロードをトリガー

2. **エージェントワークフローのテスト**
   - `/api/chat`に`{"message": "your question"}`をPOST送信
   - レスポンスの`step_history`を確認してエージェント実行パスを確認
   - `/api/workflow/graph`でワークフローグラフを表示（PNG画像）

3. **エージェント判定のデバッグ**
   - ログを確認: `make logs-dev`
   - Router判定は最初のstep_historyエントリーにある
   - Perplexityログには検索クエリと引用数が表示される

4. **新しいエージェントの追加**
   - `backend/app/agents/`にエージェントクラスを作成
   - 必要に応じて`AgentState`にステートフィールドを追加
   - `create_agent_graph()`を更新してノードとエッジを追加
   - `/api/workflow/info`をエージェントメタデータで更新

## 共通パターン

### 環境変数へのアクセス
```python
# Pythonエージェント内で
import os
api_key = os.getenv("OPENAI_API_KEY")
model = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")  # デフォルト値付き
```

### エージェント実装テンプレート
```python
class MyAgent:
    def __init__(self):
        self.llm = ChatOpenAI(model=os.getenv("OPENAI_MODEL"))
        self.prompt = ChatPromptTemplate.from_messages([...])

    async def execute(self, state: AgentState) -> AgentState:
        # ステートを処理
        chain = self.prompt | self.llm
        response = await chain.ainvoke({...})

        # ステートを更新
        state["my_field"] = response.content
        state["step_history"].append({
            "agent": "MyAgent",
            "action": "実行した内容",
            "result": response.content
        })
        return state
```

### 条件付きエッジ関数
```python
def route_function(state: AgentState) -> str:
    """ステートに基づいてノード名を文字列で返す"""
    if state.get("some_flag"):
        return "agent_a"
    else:
        return "agent_b"

workflow.add_conditional_edges(
    "source_node",
    route_function,
    {"agent_a": "agent_a", "agent_b": "agent_b"}
)
```
