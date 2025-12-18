# ステップ0: プロジェクトのセットアップ

このステップでは、LangGraphを使用したAIエージェントシステムの基盤を構築します。

## 学習ポイント

- Python仮想環境の作成
- LangGraph/LangChainのインストール
- プロジェクト構造の理解
- 環境変数の設定

## 作業ディレクトリについて

- **working-directory**: ここで実際に作業します（最初は空）
- **completed-example**: 完成形の参考実装（困ったときに参照）

## 実行手順

### 1. Claude Codeを起動

```bash
cd working-directory
claude
```

### 2. 仮想環境の作成

```
Python仮想環境を作成してください：

python3 -m venv .venv

作成後、.gitignoreファイルを作成して以下を追加：
.venv/
__pycache__/
*.pyc
.env
*.log
.pytest_cache/
```

### 3. requirements.txtの作成

```
requirements.txt ファイルを作成してください。

以下のパッケージを記述：

# LangChain / LangGraph
langchain==0.1.0
langgraph==0.0.20
langchain-anthropic==0.1.0

# API
fastapi==0.109.0
uvicorn[standard]==0.27.0
pydantic==2.5.0

# Utilities
python-dotenv==1.0.0
httpx==0.26.0

各パッケージの説明をコメントで記載してください。
```

### 4. パッケージのインストール

```
仮想環境を有効化してパッケージをインストールしてください：

# macOS/Linux
source .venv/bin/activate

# Windows
.venv\\Scripts\\activate

# インストール
pip install --upgrade pip
pip install -r requirements.txt

インストール完了後、確認：
pip list
```

### 5. ディレクトリ構造の作成

```
以下のディレクトリ構造を作成してください：

app/
├── agent/           # エージェント実装
│   ├── __init__.py
│   ├── graph.py     # LangGraphのグラフ定義
│   ├── tools.py     # カスタムツール
│   └── state.py     # ステート定義
├── api/             # FastAPI
│   ├── __init__.py
│   ├── main.py      # APIエントリーポイント
│   └── routes.py    # APIルート
└── utils/           # ユーティリティ
    ├── __init__.py
    └── config.py    # 設定管理

main.py              # アプリケーション起動

各ディレクトリに __init__.py を作成してください。
```

### 6. 環境変数ファイルの作成

```
.env ファイルを作成してください。

以下の内容を記述：

ANTHROPIC_API_KEY=
LOG_LEVEL=INFO

注意：このファイルは .gitignore に含まれています。
```

### 7. 設定ファイルの作成

```
app/utils/config.py を作成してください。

要件：
- python-dotenvを使用して環境変数を読み込み
- 設定クラスを定義
- APIキーなどの必要な設定を管理

例：
from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY')
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')

    @classmethod
    def validate(cls):
        if not cls.ANTHROPIC_API_KEY:
            raise ValueError('ANTHROPIC_API_KEY is required')

config = Config()
```

## 確認事項

以下のファイル・ディレクトリが作成されていることを確認：

- ✅ `.venv/` - 仮想環境
- ✅ `requirements.txt` - 依存関係
- ✅ `.env` - 環境変数
- ✅ `.gitignore` - Git除外設定
- ✅ `app/agent/` - エージェント実装用
- ✅ `app/api/` - API実装用
- ✅ `app/utils/` - ユーティリティ用
- ✅ `main.py` - エントリーポイント

## 動作確認

### Pythonバージョンの確認

```bash
python --version
# Python 3.10以上が必要
```

### パッケージの確認

```bash
pip show langchain langgraph
```

### 設定の読み込み確認

```
簡単なテストスクリプトを作成してください：

test_config.py

from app.utils.config import config

print(f"API Key set: {bool(config.ANTHROPIC_API_KEY)}")
print(f"Log Level: {config.LOG_LEVEL}")

実行：
python test_config.py
```

## トラブルシューティング

### Pythonバージョンが古い

```bash
# Python 3.10以上をインストール
# macOS (Homebrew)
brew install python@3.10

# Ubuntu/Debian
sudo apt install python3.10 python3.10-venv
```

### パッケージインストールエラー

```bash
# pipをアップグレード
pip install --upgrade pip

# キャッシュをクリアして再インストール
pip cache purge
pip install -r requirements.txt
```

### 仮想環境が有効化できない

```bash
# 仮想環境を削除して再作成
rm -rf .venv
python3 -m venv .venv
source .venv/bin/activate
```

## 環境変数の設定

APIキーを取得していない場合：

1. https://console.anthropic.com/ にアクセス
2. アカウント作成/ログイン
3. API Keys から新しいキーを作成
4. `.env` に設定

```env
ANTHROPIC_API_KEY=sk-ant-...
LOG_LEVEL=INFO
```

## 次のステップ

プロジェクトの基盤ができたら、次は基本的なエージェントを実装します：

👉 [01-basic-agent.md](./01-basic-agent.md) - 基本エージェント実装

---

**ヒント**:
- 仮想環境は必ず有効化してから作業
- APIキーは絶対にGitにコミットしない
- 完成例は `../completed-example/` で確認可能
- Pythonのバージョンは3.10以上を推奨
