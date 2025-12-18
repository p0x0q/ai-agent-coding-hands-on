# LangGraph Agent - AIエージェントシステムの構築

このサンプルでは、LangGraphを使用して、複数のツールを活用できるAIエージェントシステムを構築します。

## 学習目標

- LangGraphの基本概念とアーキテクチャ
- ステートマシンベースのエージェント設計
- カスタムツールの作成
- エージェントのワークフロー設計
- FastAPIでのAPI化
- ストリーミングレスポンスの実装

## 前提条件

- Python 3.10以上
- Claude Codeがインストールされていること
- Anthropic APIキー
- Pythonの基礎知識
- 仮想環境の使い方

## 難易度

⭐⭐⭐⭐☆ 中〜上級

## 所要時間

約3-4時間

## 完成イメージ

このサンプルを完成させると、以下のようなエージェントシステムができます：

- 複数のツール（検索、計算、ファイル操作など）を使いこなすエージェント
- 自律的にタスクを実行
- ステートマシンによる制御フロー
- FastAPI経由でアクセス可能
- ストリーミングレスポンス対応

## 技術スタック

- **LangGraph**: エージェントワークフローの構築
- **LangChain**: LLMとツールの統合
- **Anthropic SDK**: Claude API
- **FastAPI**: REST API
- **Pydantic**: データバリデーション
- **uvicorn**: ASGIサーバー

## ディレクトリ構成

```
langgraph-agent/
├── app/                          # Pythonアプリケーション
│   ├── agent/                   # エージェント実装
│   │   ├── __init__.py
│   │   ├── graph.py            # LangGraphのグラフ定義
│   │   ├── tools.py            # カスタムツール
│   │   └── state.py            # ステート定義
│   ├── api/                     # FastAPI
│   │   ├── __init__.py
│   │   ├── main.py             # APIエントリーポイント
│   │   └── routes.py           # APIルート
│   ├── utils/                   # ユーティリティ
│   │   └── config.py           # 設定管理
│   ├── requirements.txt         # 依存関係
│   └── main.py                  # アプリケーション起動
├── prompts/                      # プロンプト・手順書
│   ├── 01-setup.md              # プロジェクトセットアップ
│   ├── 02-basic-agent.md        # 基本エージェント実装
│   ├── 03-custom-tools.md       # カスタムツール追加
│   ├── 04-api-server.md         # API化
│   └── prompts.json             # 再利用可能なプロンプト
└── README.md                     # このファイル
```

## 進め方

### ステップ1: 環境構築

1. このディレクトリに移動
   ```bash
   cd claude-code/langgraph-agent
   ```

2. 仮想環境を作成・有効化
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # macOS/Linux
   # または
   .venv\Scripts\activate  # Windows
   ```

3. プロンプトに従ってセットアップ
   👉 [prompts/01-setup.md](./prompts/01-setup.md)

### ステップ2: 基本エージェント実装

4. LangGraphで基本的なエージェントを構築
   👉 [prompts/02-basic-agent.md](./prompts/02-basic-agent.md)

### ステップ3: カスタムツール追加

5. 独自のツールを作成してエージェントに追加
   👉 [prompts/03-custom-tools.md](./prompts/03-custom-tools.md)

### ステップ4: API化

6. FastAPIでRESTful APIとして公開
   👉 [prompts/04-api-server.md](./prompts/04-api-server.md)

## LangGraphの基礎

### ステートマシンの概念

LangGraphは、エージェントの動作をステートマシンとして定義します：

```python
from langgraph.graph import StateGraph

# ステート定義
class AgentState(TypedDict):
    messages: list[Message]
    next_step: str

# グラフ作成
workflow = StateGraph(AgentState)

# ノード追加
workflow.add_node("agent", agent_node)
workflow.add_node("tools", tool_node)

# エッジ定義
workflow.add_edge("agent", "tools")
workflow.add_conditional_edges("tools", should_continue)
```

### ノードとエッジ

- **ノード**: 処理を行う場所（例：LLM呼び出し、ツール実行）
- **エッジ**: ノード間の遷移（例：条件分岐）

## 学べるポイント

### 1. LangGraphアーキテクチャ

- ステートグラフの設計
- ノードとエッジの定義
- 条件分岐の実装
- ループ処理の制御

### 2. カスタムツール開発

- ツールの抽象化
- 入力バリデーション
- エラーハンドリング
- ツールの登録

### 3. エージェント設計

- ReActパターンの理解
- ツール選択のロジック
- コンテキスト管理
- タスク分解

### 4. FastAPI統合

- APIエンドポイントの設計
- 非同期処理
- ストリーミングレスポンス
- CORS設定

## 環境変数の設定

`.env` ファイルを作成：

```env
ANTHROPIC_API_KEY=your_api_key_here
LANGSMITH_API_KEY=your_langsmith_key_here  # オプション
LOG_LEVEL=INFO
```

## エージェントの実行

### コマンドラインから

```bash
python app/main.py "東京の天気を調べて、おすすめの服装を教えて"
```

### APIサーバーとして

```bash
# サーバー起動
uvicorn app.api.main:app --reload

# リクエスト
curl -X POST http://localhost:8000/agent/run \
  -H "Content-Type: application/json" \
  -d '{"message": "計算: 123 * 456"}'
```

## カスタムツールの例

### 1. Web検索ツール

```python
from langchain.tools import tool

@tool
def web_search(query: str) -> str:
    """指定されたクエリでWeb検索を実行"""
    # 実装
    return results
```

### 2. ファイル操作ツール

```python
@tool
def read_file(file_path: str) -> str:
    """ファイルの内容を読み込む"""
    with open(file_path, 'r') as f:
        return f.read()
```

### 3. データベースツール

```python
@tool
def query_database(sql: str) -> dict:
    """SQLクエリを実行してデータを取得"""
    # 実装
    return results
```

## よくある質問

### Q: LangGraphとLangChainの違いは？

A: LangChainはツールやLLMの統合ライブラリ、LangGraphはそれらを組み合わせて複雑なワークフローを構築するためのフレームワークです。

### Q: どんな場合にLangGraphを使うべき？

A: 以下の場合に有効です：
- 複数のステップが必要なタスク
- 条件分岐やループが必要
- 複数のツールを組み合わせる
- 状態を管理する必要がある

### Q: ReActパターンとは？

A: Reasoning（推論）とActing（行動）を交互に行うパターンです。エージェントが思考→行動→観察を繰り返します。

## トラブルシューティング

### インポートエラー

```bash
# 仮想環境が有効化されているか確認
which python

# 依存関係を再インストール
pip install -r requirements.txt
```

### LangSmithの設定

```python
# LangSmithでのトレースを有効化（オプション）
import os
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "langgraph-agent"
```

### エージェントが無限ループ

```
# Claude Codeに質問
エージェントが同じツールを繰り返し呼び出して
無限ループしています。

ループ検出と終了条件を追加してください。
最大イテレーション数を設定し、
同じアクションの繰り返しを防ぐロジックを実装してください。
```

## 応用課題

### 1. マルチエージェントシステム

```
複数のエージェントが協調して動作するシステムを構築してください。

例：
- 研究エージェント：情報収集
- 分析エージェント：データ分析
- レポートエージェント：結果をまとめる
```

### 2. メモリ機能の追加

```
エージェントが過去の会話を記憶できるように、
メモリ機能を実装してください。

要件：
- 短期記憶（セッション内）
- 長期記憶（永続化）
- ベクトルDBでの類似検索
```

### 3. 並列ツール実行

```
複数のツールを並列で実行できるように拡張してください。

例：
- 複数のWebサイトを同時検索
- 複数のAPIを並列呼び出し
```

### 4. ヒューマン・イン・ザ・ループ

```
重要な決定前にユーザーの承認を求める機能を追加してください。

例：
- ファイル削除前の確認
- 高額な操作の承認
```

### 5. エラーリカバリー

```
ツールの実行失敗時に、自動的にリトライや
代替手段を試す機能を実装してください。
```

## アーキテクチャパターン

### 1. ReActエージェント

```python
# 思考 → 行動 → 観察のサイクル
def react_agent(state):
    # 1. 思考（Reasoning）
    thought = llm.think(state)

    # 2. 行動（Acting）
    action = select_tool(thought)
    result = execute_tool(action)

    # 3. 観察（Observation）
    observation = process_result(result)

    return updated_state
```

### 2. プランニング型エージェント

```python
# 最初に計画を立ててから実行
def planning_agent(state):
    # 1. 計画立案
    plan = create_plan(state.task)

    # 2. 計画実行
    for step in plan:
        execute_step(step)

    # 3. 結果統合
    return final_result
```

### 3. 階層型エージェント

```python
# 複数のサブエージェントを管理
def hierarchical_agent(state):
    # タスクを分解
    subtasks = decompose_task(state.task)

    # サブエージェントに委譲
    results = [
        sub_agent.run(subtask)
        for subtask in subtasks
    ]

    # 結果を統合
    return combine_results(results)
```

## パフォーマンス最適化

### 1. キャッシング

```python
from functools import lru_cache

@lru_cache(maxsize=100)
def expensive_operation(input):
    # 重い処理
    return result
```

### 2. 非同期処理

```python
import asyncio

async def async_tool_execution(tools):
    results = await asyncio.gather(*[
        tool.arun() for tool in tools
    ])
    return results
```

### 3. バッチ処理

```python
# 複数のリクエストをまとめて処理
def batch_process(requests):
    return llm.batch(requests)
```

## セキュリティ考慮事項

- ✅ ツールの実行権限を制限
- ✅ ユーザー入力のサニタイズ
- ✅ APIキーの安全な管理
- ✅ ファイルアクセスの制限
- ✅ コマンドインジェクション対策

## 次のステップ

1. [nextjs-chat-app](../nextjs-chat-app) と統合してフルスタックアプリを構築
2. より複雑なマルチエージェントシステムに挑戦
3. プロダクション環境へのデプロイ

## 参考リソース

- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [LangChain Documentation](https://python.langchain.com/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [ReAct Paper](https://arxiv.org/abs/2210.03629)

---

質問や問題があれば、[Issues](https://github.com/yourusername/ai-agent-coding-hands-on/issues)で報告してください！
