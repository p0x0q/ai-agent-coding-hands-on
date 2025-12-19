.PHONY: help serve-dev serve-prod build-dev build-prod down-dev down-prod logs-dev logs-prod clean restart-dev restart-prod

# デフォルトターゲット
help:
	@echo "AI Multi-Agent Hackathon - Make Commands"
	@echo ""
	@echo "開発環境:"
	@echo "  make serve-dev      - 開発環境を起動（ホットリロード有効）"
	@echo "  make build-dev      - 開発環境をビルド"
	@echo "  make restart-dev    - 開発環境を再起動"
	@echo "  make logs-dev       - 開発環境のログを表示"
	@echo "  make down-dev       - 開発環境を停止"
	@echo ""
	@echo "本番環境:"
	@echo "  make serve-prod     - 本番環境を起動"
	@echo "  make build-prod     - 本番環境をビルド"
	@echo "  make restart-prod   - 本番環境を再起動"
	@echo "  make logs-prod      - 本番環境のログを表示"
	@echo "  make down-prod      - 本番環境を停止"
	@echo ""
	@echo "その他:"
	@echo "  make clean          - すべてのコンテナとボリュームを削除"
	@echo "  make help           - このヘルプを表示"

# 開発環境コマンド
serve-dev:
	@echo "🚀 開発環境を起動中..."
	docker compose -f docker-compose.dev.yaml up -d
	@echo "✅ 開発環境が起動しました"
	@echo "   フロントエンド: http://localhost:3000"
	@echo "   バックエンドAPI: http://localhost:8002"
	@echo "   API ドキュメント: http://localhost:8002/docs"

build-dev:
	@echo "🔨 開発環境をビルド中..."
	docker compose -f docker-compose.dev.yaml build
	@echo "✅ ビルド完了"

restart-dev:
	@echo "🔄 開発環境を再起動中..."
	docker compose -f docker-compose.dev.yaml restart
	@echo "✅ 再起動完了"

logs-dev:
	docker compose -f docker-compose.dev.yaml logs -f

down-dev:
	@echo "🛑 開発環境を停止中..."
	docker compose -f docker-compose.dev.yaml down
	@echo "✅ 停止完了"

# 本番環境コマンド
serve-prod:
	@echo "🚀 本番環境を起動中..."
	docker compose -f docker-compose.prod.yaml up -d --build
	@echo "✅ 本番環境が起動しました"
	@echo "   フロントエンド: http://localhost:3000"
	@echo "   バックエンドAPI: http://localhost:8002"
	@echo "   API ドキュメント: http://localhost:8002/docs"

build-prod:
	@echo "🔨 本番環境をビルド中..."
	docker compose -f docker-compose.prod.yaml build
	@echo "✅ ビルド完了"

restart-prod:
	@echo "🔄 本番環境を再起動中..."
	docker compose -f docker-compose.prod.yaml restart
	@echo "✅ 再起動完了"

logs-prod:
	docker compose -f docker-compose.prod.yaml logs -f

down-prod:
	@echo "🛑 本番環境を停止中..."
	docker compose -f docker-compose.prod.yaml down
	@echo "✅ 停止完了"

# クリーンアップ
clean:
	@echo "🧹 すべてのコンテナとボリュームを削除中..."
	docker compose -f docker-compose.dev.yaml down -v 2>/dev/null || true
	docker compose -f docker-compose.prod.yaml down -v 2>/dev/null || true
	docker compose down -v 2>/dev/null || true
	@echo "✅ クリーンアップ完了"

# コンテナの状態確認
status:
	@echo "📊 コンテナの状態:"
	@docker ps -a | grep langgraph-nextjs || echo "起動中のコンテナはありません"
