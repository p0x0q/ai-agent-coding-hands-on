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
├── frontend/              # Next.js 15 アプリケーション
│   ├── src/
│   │   ├── app/          # App Router
│   │   ├── components/   # Reactコンポーネント
│   │   └── lib/          # ユーティリティ
│   ├── Dockerfile
│   └── package.json
│
├── backend/              # Python バックエンド
│   ├── app/
│   │   ├── agents/      # LangGraphエージェント定義
│   │   ├── api/         # FastAPI ルート
│   │   ├── services/    # ビジネスロジック
│   │   └── main.py      # エントリーポイント
│   ├── Dockerfile
│   └── requirements.txt
│
├── docker-compose.yaml   # 統合起動設定
├── .env                  # 環境変数(OpenAI APIキー等)
└── README.md            # このファイル
```

## マルチエージェント設計(LangGraph)

### エージェント構成
以下の3つの専門エージェントで協調動作するシステムを構築:

1. **Researcher Agent(リサーチャー)**
   - 役割: ユーザーの質問を分析し、必要な情報を収集
   - 機能: Web検索、データ収集、情報整理

2. **Analyzer Agent(アナライザー)**
   - 役割: 収集された情報を分析・評価
   - 機能: データ分析、パターン認識、洞察抽出

3. **Composer Agent(コンポーザー)**
   - 役割: 分析結果を統合し、最終的な回答を生成
   - 機能: 回答生成、フォーマット整形、品質確認

### ワークフロー
```
[ユーザー入力]
    ↓
[Researcher] → 情報収集
    ↓
[Analyzer] → データ分析
    ↓
[Composer] → 回答生成
    ↓
[ユーザーへ出力]
```

### LangGraph State管理
```python
class AgentState(TypedDict):
    user_query: str           # ユーザーの質問
    research_data: List[str]  # 収集した情報
    analysis_result: Dict     # 分析結果
    final_answer: str         # 最終回答
    step_history: List[str]   # 実行履歴
```

## APIエンドポイント設計

### Backend API (FastAPI)
- `POST /api/chat` - チャットメッセージ送信
- `GET /api/chat/stream` - ストリーミングレスポンス(SSE)
- `GET /api/agents/status` - エージェント状態確認
- `GET /api/health` - ヘルスチェック

### Frontend Routes
- `/` - メインチャット画面
- `/history` - 会話履歴
- `/agents` - エージェント動作可視化

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
