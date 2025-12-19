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
git clone https://github.com/p0x0q/ai-agent-coding-hands-on.git
cd ai-agent-coding-hands-on

# サンプルアプリのディレクトリに移動（例：hello-claude）
cd claude-code/hello-claude
```

## 5. 環境変数の設定

各サンプルアプリで `.env.example` ファイルがある場合は、コピーして編集します：

```bash
cp .env.example .env
```

## 6. サンプルアプリの起動確認

基本的にMakefileが用意されているので、以下のコマンドで起動できます。
docker compose環境が必要です。

```bash
make serve-dev
```

ブラウザで `http://localhost:3000` を開いて確認します。
