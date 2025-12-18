# Python開発環境用Dockerfile
FROM python:3.10-slim

WORKDIR /app

# システムパッケージの更新
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# requirements.txtをコピー
COPY requirements.txt .

# Pythonパッケージをインストール
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# アプリケーションファイルをコピー
COPY . .

# ポート8000を公開
EXPOSE 8000

# FastAPIサーバーを起動
CMD ["uvicorn", "app.api.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
