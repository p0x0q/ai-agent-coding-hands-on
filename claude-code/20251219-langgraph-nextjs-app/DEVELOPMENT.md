# 開発ガイド

## ホットリロード対応

このプロジェクトは開発環境と本番環境で別々のDocker Compose設定を使用しています。

### 開発環境（ホットリロード有効）

開発環境ではコード変更が自動的に反映されます。

```bash
# 開発環境を起動
make serve-dev

# ログを確認
make logs-dev

# 再起動
make restart-dev

# 停止
make down-dev
```

**ホットリロードの動作**:
- **フロントエンド**: app/, components/, lib/, 設定ファイルの変更が即座に反映
- **バックエンド**: app/配下のPythonファイル変更が自動リロード

### 本番環境

本番環境では最適化されたビルドを使用します。

```bash
# 本番環境を起動
make serve-prod

# ログを確認
make logs-prod

# 停止
make down-prod
```

## Makeコマンド一覧

```bash
make help           # ヘルプを表示
make serve-dev      # 開発環境を起動
make serve-prod     # 本番環境を起動
make build-dev      # 開発環境をビルド
make build-prod     # 本番環境をビルド
make restart-dev    # 開発環境を再起動
make restart-prod   # 本番環境を再起動
make logs-dev       # 開発環境のログを表示
make logs-prod      # 本番環境のログを表示
make down-dev       # 開発環境を停止
make down-prod      # 本番環境を停止
make clean          # すべてのコンテナとボリュームを削除
make status         # コンテナの状態を確認
```

## ディレクトリ構成

### フロントエンド
```
frontend/
├── app/              # Next.js App Router (ホットリロード対象)
├── components/       # Reactコンポーネント (ホットリロード対象)
├── lib/             # ユーティリティ (ホットリロード対象)
├── public/          # 静的ファイル (ホットリロード対象)
├── Dockerfile       # 本番用Dockerfile
├── Dockerfile.dev   # 開発用Dockerfile
└── package.json
```

### バックエンド
```
backend/
├── app/
│   ├── agents/      # LangGraphエージェント (ホットリロード対象)
│   ├── api/         # FastAPI ルート (ホットリロード対象)
│   ├── services/    # ビジネスロジック (ホットリロード対象)
│   ├── models/      # データモデル (ホットリロード対象)
│   └── main.py      # エントリーポイント (ホットリロード対象)
├── Dockerfile       # 本番用Dockerfile
└── requirements.txt
```

## 開発環境の設定

### docker-compose.dev.yaml
- フロントエンド: `npm run dev`で起動
- バックエンド: `uvicorn --reload`で起動
- 主要ファイルがvolumeマウントされ、変更が即座に反映

### docker-compose.prod.yaml
- フロントエンド: standalone buildで最適化
- バックエンド: 通常のuvicorn起動
- volumeマウントなし

## トラブルシューティング

### フロントエンドの変更が反映されない
```bash
# コンテナを再起動
make restart-dev

# それでもダメな場合は再ビルド
make down-dev
make build-dev
make serve-dev
```

### バックエンドの変更が反映されない
```bash
# Pythonキャッシュをクリア
docker exec langgraph-nextjs-backend-dev find /app -type d -name __pycache__ -exec rm -rf {} +

# コンテナを再起動
make restart-dev
```

### ポート競合エラー
```bash
# すべてのコンテナを停止
make clean

# 再度起動
make serve-dev
```

## 環境変数

`.env`ファイルで以下を設定:
```bash
OPENAI_API_KEY=your-api-key
OPENAI_MODEL=gpt-4.1-mini
PERPLEXITY_API_KEY=your-perplexity-key
```

開発環境では以下の追加設定が有効:
- `PYTHONDONTWRITEBYTECODE=1` - .pycファイルを生成しない
- `PYTHONUNBUFFERED=1` - ログをバッファリングしない
- `NODE_ENV=development` - Next.js開発モード

## デバッグ

### ログの確認
```bash
# すべてのログ
make logs-dev

# バックエンドのみ
docker compose -f docker-compose.dev.yaml logs -f backend

# フロントエンドのみ
docker compose -f docker-compose.dev.yaml logs -f frontend
```

### コンテナ内でシェルを実行
```bash
# バックエンド
docker exec -it langgraph-nextjs-backend-dev sh

# フロントエンド
docker exec -it langgraph-nextjs-frontend-dev sh
```

## パフォーマンス

### ビルド時間の短縮
- 開発環境では必要最小限のファイルのみマウント
- node_modulesは名前付きボリュームを使用してI/O負荷を軽減

### ホットリロード速度
- **フロントエンド**: Next.js Fast Refreshで即座に反映（通常1秒以内）
- **バックエンド**: uvicorn watchfilesで自動リロード（通常2-3秒）
