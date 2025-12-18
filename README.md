# AI Agent Coding Hands-on

**本リポジトリは、2025/12/19までに整備しますので、ご注意ください。リポジトリクローンされている方は、最新Mainで同期いただく必要があります。**

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
├── app/                          # アプリケーション本体のコード
├── prompts/                      # プロンプトや手順書
│   ├── 01-setup.md              # セットアップ手順
│   ├── 02-implementation.md     # 実装手順とプロンプト
│   └── prompts.json             # 再利用可能なプロンプト集
└── README.md                     # サンプルの説明
```

## クイックスタート

### 1. リポジトリをクローン

```bash
git clone https://github.com/yourusername/ai-agent-coding-hands-on.git
cd ai-agent-coding-hands-on
```

### 2. 環境構築

詳細な環境構築方法は [docs/getting-started.md](docs/getting-started.md) を参照してください。

### 3. サンプルを選んで開始

1. `claude-code/` ディレクトリから興味のあるサンプルを選ぶ
2. 各サンプルの `README.md` を読む
3. `prompts/` ディレクトリの手順に従って実装を進める

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

質問や問題がある場合は、[Issues](https://github.com/yourusername/ai-agent-coding-hands-on/issues) で報告してください。

---

Happy AI-Driven Development!
