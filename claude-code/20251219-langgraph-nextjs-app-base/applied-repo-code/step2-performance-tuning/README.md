# AIハッカソン - マルチエージェントアプリケーション

## プロジェクト概要
LangGraphを使用したマルチエージェントシステムのデモアプリケーション。
フロントエンドにNext.js 15、バックエンドにPython 3.11を使用し、Docker Composeで一括起動可能な構成。

## アーキテクチャ設計

### 技術スタック
- **フロントエンド**: Next.js 15 (App Router)
  - TypeScript
  - React 19
  - Tailwind CSS
  - WebSocket/Server-Sent Events (リアルタイム通信)

- **バックエンド**: Python 3.11
  - FastAPI (APIサーバー)
  - LangGraph (マルチエージェントオーケストレーション)
  - LangChain
  - OpenAI API (gpt-4.1-mini)

- **インフラ**: Docker Compose
  - Frontend container
  - Backend container
  - 環境変数管理

### ディレクトリ構造
```
.
├── frontend/                  # Next.js 15 アプリケーション
│   ├── app/                   # App Router
│   │   ├── globals.css
│   │   ├── layout.tsx
│   │   └── page.tsx
│   ├── components/            # Reactコンポーネント
│   │   ├── ChatInterface.tsx
│   │   └── WorkflowViewer.tsx
│   ├── lib/                   # ユーティリティ
│   ├── public/                # 静的ファイル
│   ├── Dockerfile             # 本番用
│   ├── Dockerfile.dev         # 開発用
│   ├── next.config.ts
│   ├── package.json
│   ├── tailwind.config.ts
│   └── tsconfig.json
│
├── backend/                   # Python 3.11 バックエンド
│   ├── app/
│   │   ├── agents/           # LangGraphエージェント
│   │   │   ├── analyzer.py   # Analyzer Agent
│   │   │   ├── composer.py   # Composer Agent
│   │   │   ├── graph.py      # LangGraphワークフロー
│   │   │   ├── researcher.py # Researcher Agent
│   │   │   ├── router.py     # Router Agent
│   │   │   └── state.py      # 共有ステート定義
│   │   ├── api/              # FastAPI ルート
│   │   │   └── chat.py
│   │   ├── models/           # データモデル
│   │   │   └── schemas.py
│   │   ├── services/         # 外部サービス連携
│   │   │   └── perplexity.py
│   │   └── main.py           # FastAPIエントリーポイント
│   ├── Dockerfile
│   └── requirements.txt
│
├── tutorial-prompts/          # チュートリアル用プロンプト
│   └── STEP1.md
│
├── docker-compose.yaml        # 基本Docker構成
├── docker-compose.dev.yaml    # 開発環境構成
├── docker-compose.prod.yaml   # 本番環境構成
├── Makefile                   # 開発用コマンド
├── .env                       # 環境変数(OpenAI APIキー等)
├── CLAUDE.md                  # Claude Code向けガイド
├── DEVELOPMENT.md             # 開発ドキュメント
├── SETUP.md                   # セットアップガイド
└── README.md                  # このファイル
```

## マルチエージェント設計(LangGraph)

### エージェント構成
以下の4つの専門エージェントで協調動作するシステムを構築:

1. **Router Agent(ルーター)**
   - 役割: ユーザーの質問を分析し、Web検索が必要かを判断
   - 機能: クエリ分析、条件付きルーティング、コンテキスト評価
   - 出力: `needs_research`フラグを設定

2. **Researcher Agent(リサーチャー)**
   - 役割: Web検索が必要な場合のみ、情報を収集
   - 機能: Perplexity APIを使用したWeb検索、データ収集、引用付き結果の整理
   - 条件: `needs_research=True`の場合のみ実行

3. **Analyzer Agent(アナライザー)**
   - 役割: 収集された検索結果を分析・評価
   - 機能: データ分析、パターン認識、洞察抽出
   - 条件: Researcherの後にのみ実行

4. **Composer Agent(コンポーザー)**
   - 役割: 最終的な回答を生成
   - 機能: 回答生成、フォーマット整形、会話コンテキストの活用
   - 実行: すべてのパスで最終ステップとして実行

### ワークフロー

**Web検索が必要な場合** (`needs_research=True`):
```
[ユーザー入力]
    ↓
[Router] → クエリ分析・ルーティング判定
    ↓
[Researcher] → Perplexity APIでWeb検索
    ↓
[Analyzer] → 検索結果の分析
    ↓
[Composer] → 最終回答生成
    ↓
[ユーザーへ出力]
```

**一般的な知識で回答可能な場合** (`needs_research=False`):
```
[ユーザー入力]
    ↓
[Router] → クエリ分析・ルーティング判定
    ↓
[Composer] → 最終回答生成（直接パス）
    ↓
[ユーザーへ出力]
```

### LangGraph State管理
```python
class AgentState(TypedDict):
    user_query: str                    # ユーザーの質問
    conversation_history: List[Dict]   # 会話履歴（コンテキスト用）
    needs_research: bool               # Web検索が必要かのフラグ
    messages: Annotated[List, add_messages]  # LangGraphメッセージ履歴
    research_data: str                 # 収集した検索結果
    analysis_result: str               # 分析結果
    final_answer: str                  # 最終回答
    step_history: List[Dict]           # エージェント実行履歴
```

## APIエンドポイント設計

### Backend API (FastAPI)
- `POST /api/chat` - チャットメッセージ送信、エージェントグラフを実行
- `GET /api/workflow/graph` - LangGraphのPNG可視化を返す
- `GET /api/workflow/info` - エージェントメタデータと説明を返す
- `GET /health` - ヘルスチェック

### Frontend Routes
- `/` - メインチャット画面（ChatInterfaceコンポーネント）
  - チャット入出力
  - WorkflowViewerコンポーネントでエージェントワークフロー可視化

## 環境変数

`.env`ファイルに以下を設定済み:
```bash
OPENAI_API_KEY=<your-api-key>
OPENAI_MODEL=gpt-5
PERPLEXITY_API_KEY=<your-perplexity-api-key>
```

実際の.envファイルには既にAPIキーが設定されています。

## セットアップ・起動方法

### 前提条件
- Docker Desktop インストール済み
- `.env`ファイルにOPENAI_API_KEYが設定済み

### 起動コマンド（Makefileを使用）

**開発環境（ホットリロード有効）**:
```bash
# 開発環境を起動
make serve-dev

# ログ確認
make logs-dev

# 停止
make down-dev
```

**本番環境**:
```bash
# 本番環境を起動
make serve-prod

# 停止
make down-prod
```

**その他のコマンド**:
```bash
# ヘルプを表示
make help

# すべてクリーンアップ
make clean
```

詳細は [DEVELOPMENT.md](./DEVELOPMENT.md) を参照してください。

### アクセスURL
- フロントエンド: http://localhost:3000
- バックエンドAPI: http://localhost:8002
- API ドキュメント: http://localhost:8002/docs

## 開発フロー

1. **Phase 1: 基盤構築**
   - ディレクトリ作成・初期化
   - Docker環境構築
   - 基本的なNext.js/FastAPIセットアップ

2. **Phase 2: LangGraphエージェント実装**
   - 各エージェントの実装
   - ステートグラフの構築
   - エージェント間通信の実装

3. **Phase 3: UI/UX構築**
   - チャットインターフェース
   - エージェント動作の可視化
   - ストリーミング対応

4. **Phase 4: 統合・テスト**
   - E2Eテスト
   - パフォーマンス最適化
   - エラーハンドリング

## 特徴・差別化ポイント

- **リアルタイム可視化**: エージェントの思考プロセスを可視化
- **ストリーミング対応**: 回答を逐次表示してUX向上
- **モジュラー設計**: エージェントの追加・変更が容易
- **Docker統合**: 環境構築が簡単で再現性が高い

## 今後の拡張案

- エージェントの追加(例: Validator, Critic)
- 永続化層の追加(PostgreSQL/Redis)
- 認証・ユーザー管理
- マルチモーダル対応(画像・音声)
- カスタムツール統合

---

**レビューポイント**:
- エージェント構成は適切か?
- ワークフローは妥当か?
- 技術スタック選定に問題はないか?
- 追加したい機能や変更したい点はあるか?
