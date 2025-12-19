# AI Agent Coding Hands-on

** 2025/12/19 ハンズオン参加者向け: [./claude-code/20251219-langgraph-nextjs-app-base](./claude-code/20251219-langgraph-nextjs-app-base) 下のディレクトリを利用しますので、こちらを参照してください。**

AI駆動開発を実践的に学ぶためのハンズオンリポジトリです。Claude CodeをはじめとするAI開発ツールを使って、実際のアプリケーション開発を体験できます。

## 目的

このリポジトリは、AI駆動開発の実践的なスキルを習得することを目的としています：

- AI開発ツールの効果的な使い方を学ぶ
- 実際のアプリケーション開発を通じて、AIとの協働方法を体得する
- TypeScript/Next.jsとPython/LangGraphを組み合わせたモダンな開発手法を習得する
- 再利用可能なプロンプトパターンを蓄積する

## 対象者

- AI駆動開発に興味がある全てのエンジニア
- 初心者から上級者まで、レベルに応じたサンプルを用意しています
- Claude Codeの使い方を学びたい方

## リポジトリ構成

```
ai-agent-coding-hands-on/
├── README.md                      # このファイル
├── docs/                          # 全般的なドキュメント
│   ├── getting-started.md        # 環境構築・始め方
│   └── best-practices.md         # ベストプラクティス集
├── claude-code/                   # Claude Code用サンプル
│   ├── hello-claude/             # 初心者向け：基本操作を学ぶ
│   ├── nextjs-chat-app/          # 中級者向け：Next.jsでAIチャットアプリ
│   ├── langgraph-agent/          # 中級者向け：LangGraphでエージェント作成
│   └── README.md                 # Claude Code全般の説明
└── cursor/                        # 将来的に追加予定
```

### 各サンプルの構成

各サンプルディレクトリは以下の構成になっています：

```
sample-name/
├── working-directory/            # 作業ディレクトリ（ここで実装）
│   └── (空 - プロンプトに従って作成)
├── completed-example/            # 完成例（参考用）
│   ├── (実装済みコード)
│   ├── (テストコード)
│   └── README.md                # 実行方法と解説
├── prompts/                      # プロンプトや手順書
│   ├── 00-setup.md              # セットアップ手順
│   ├── 01-xxx.md                # ステップ1
│   ├── 02-xxx.md                # ステップ2
│   └── prompts.json             # 再利用可能なプロンプト集
└── README.md                     # サンプルの説明
```

**学習の流れ**：
1. `prompts/` の手順書に従って、`working-directory/` で実装
2. わからなくなったら `completed-example/` を参照
3. 最終的に完成例と同じものができる

## クイックスタート

### 1. リポジトリをクローン

```bash
git clone https://github.com/p0x0q/ai-agent-coding-hands-on.git
cd ai-agent-coding-hands-on
```

### 2. 環境構築

詳細な環境構築方法は [docs/getting-started.md](docs/getting-started.md) を参照してください。

### 3. サンプルを選んで開始

1. `claude-code/` ディレクトリから興味のあるサンプルを選ぶ
2. 各サンプルの `README.md` を読む
3. `working-directory/` に移動して Claude Code を起動
4. `prompts/` ディレクトリの手順（00-setup.md から順番）に従って実装
5. 困ったら `completed-example/` の完成例を参照

### Docker Composeでの起動（推奨）

各サンプルは Docker Compose に対応しています：

```bash
# 例：hello-claude を起動
cd claude-code/hello-claude
docker-compose up

# バックグラウンド起動
docker-compose up -d

# 停止
docker-compose down
```

**ポート番号**：
- hello-claude: 8000 (作業), 8001 (完成例)
- nextjs-chat-app: 3000 (作業), 3001 (完成例)
- langgraph-agent: 8000 (作業), 8001 (完成例)

## 推奨する学習順序

### 初心者向け

1. [claude-code/hello-claude](claude-code/hello-claude) - Claude Codeの基本操作を学ぶ

### 中級者向け

2. [claude-code/nextjs-chat-app](claude-code/nextjs-chat-app) - Next.jsでAIチャットアプリを構築
3. [claude-code/langgraph-agent](claude-code/langgraph-agent) - LangGraphでエージェントシステムを作成

### 上級者向け

4. 複数のサンプルを組み合わせて、独自のアプリケーションを構築

## 技術スタック

このリポジトリで扱う主な技術：

- **フロントエンド**: TypeScript, Next.js, React
- **バックエンド**: Python, FastAPI, LangGraph
- **AI開発ツール**: Claude Code (メイン), その他追加予定
- **その他**: Tailwind CSS, Prisma, PostgreSQL など

## ベストプラクティス

効果的なAI駆動開発のためのベストプラクティスは [docs/best-practices.md](docs/best-practices.md) を参照してください。

## コントリビューション

このリポジトリへの貢献を歓迎します！

- 新しいサンプルの追加
- ドキュメントの改善
- バグ修正や改善提案

詳細は [CONTRIBUTING.md](CONTRIBUTING.md) を参照してください（準備中）。

## ライセンス

MIT License

## 関連リンク

- [Claude Code 公式ドキュメント](https://docs.anthropic.com/claude/docs)
- [LangGraph ドキュメント](https://langchain-ai.github.io/langgraph/)
- [Next.js ドキュメント](https://nextjs.org/docs)

## サポート

質問や問題がある場合は、[Issues](https://github.com/p0x0q/ai-agent-coding-hands-on/issues) で報告してください。

---

Happy AI-Driven Development!
