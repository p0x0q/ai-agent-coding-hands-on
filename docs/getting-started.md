# Getting Started - 環境構築ガイド

このガイドでは、AI Agent Coding Hands-onを始めるための環境構築手順を説明します。

## 前提条件

以下のツールがインストールされていることを確認してください：

- **Node.js**: v18以上
- **Python**: v3.10以上
- **Git**: 最新版
- **Claude Code**: Anthropic公式CLI（後述の手順でインストール）

## 1. Claude Codeのセットアップ

### インストール

```bash
# npmを使用してインストール
npm install -g @anthropic-ai/claude-code

# または、Homebrewを使用（macOS/Linux）
brew install claude-code
```

### 認証設定

```bash
# Claude Codeにログイン
claude auth login

# APIキーの設定（必要に応じて）
claude auth set-api-key YOUR_API_KEY
```

### 動作確認

```bash
# バージョン確認
claude --version

# ヘルプ表示
claude --help
```

## 2. Node.js環境のセットアップ

### パッケージマネージャーの選択

このリポジトリでは、以下のいずれかを推奨します：

- **npm**: Node.jsに標準で付属
- **pnpm**: 高速で効率的（推奨）
- **yarn**: 広く使われている

pnpmのインストール（推奨）：

```bash
npm install -g pnpm
```

## 3. Python環境のセットアップ

### 仮想環境の作成

```bash
# venvを使用した仮想環境の作成
python3 -m venv .venv

# 仮想環境の有効化
# macOS/Linux:
source .venv/bin/activate

# Windows:
.venv\Scripts\activate
```

### 必要なパッケージのインストール

```bash
# 基本的なパッケージ
pip install --upgrade pip
pip install langchain langgraph langsmith
pip install fastapi uvicorn
pip install python-dotenv
```

## 4. リポジトリのクローンと初期設定

```bash
# リポジトリをクローン
git clone https://github.com/yourusername/ai-agent-coding-hands-on.git
cd ai-agent-coding-hands-on

# サンプルアプリのディレクトリに移動（例：hello-claude）
cd claude-code/hello-claude
```

## 5. 環境変数の設定

各サンプルアプリで `.env.example` ファイルがある場合は、コピーして編集します：

```bash
cp .env.example .env
```

`.env` ファイルに必要な情報を記入：

```env
# Anthropic API Key
ANTHROPIC_API_KEY=your_api_key_here

# その他のAPI Keys（必要に応じて）
OPENAI_API_KEY=your_openai_key_here
LANGSMITH_API_KEY=your_langsmith_key_here
```

## 6. サンプルアプリの起動確認

### Next.jsアプリの場合

```bash
cd claude-code/nextjs-chat-app/app

# 依存関係のインストール
pnpm install

# 開発サーバーの起動
pnpm dev
```

ブラウザで `http://localhost:3000` を開いて確認します。

### Pythonアプリの場合

```bash
cd claude-code/langgraph-agent/app

# 依存関係のインストール
pip install -r requirements.txt

# アプリの起動
python main.py
```

## トラブルシューティング

### Claude Codeが起動しない

```bash
# キャッシュをクリア
claude cache clear

# 再認証
claude auth logout
claude auth login
```

### Node.jsのバージョン問題

```bash
# nvmを使用してバージョンを管理
nvm install 18
nvm use 18
```

### Pythonの依存関係エラー

```bash
# 仮想環境を再作成
deactivate
rm -rf .venv
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 次のステップ

環境構築が完了したら、以下を試してみましょう：

1. [claude-code/hello-claude](../claude-code/hello-claude) で基本操作を学ぶ
2. [best-practices.md](./best-practices.md) でベストプラクティスを確認
3. 自分の興味に応じたサンプルプロジェクトを選ぶ

## 参考リンク

- [Claude Code 公式ドキュメント](https://docs.anthropic.com/claude/docs)
- [Node.js 公式サイト](https://nodejs.org/)
- [Python 公式サイト](https://www.python.org/)
- [LangGraph ドキュメント](https://langchain-ai.github.io/langgraph/)

---

問題が解決しない場合は、[Issues](https://github.com/yourusername/ai-agent-coding-hands-on/issues) で質問してください。
