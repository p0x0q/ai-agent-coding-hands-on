# ステップ0: プロジェクトのセットアップ

このステップでは、Next.js 14とClaude APIを使ったチャットアプリケーションの基盤を構築します。

## 学習ポイント

- Next.js App Routerのプロジェクト作成
- TypeScriptの設定
- 必要なパッケージのインストール
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

### 2. Next.jsプロジェクトの作成

以下のプロンプトをClaude Codeに入力：

```
Next.js 14のプロジェクトを作成してください。

要件：
- App Routerを使用
- TypeScriptを使用
- Tailwind CSSを使用
- ESLintを設定
- src/ディレクトリを使用

以下のコマンドを実行してプロジェクトを作成してください：
npx create-next-app@latest . --typescript --tailwind --app --src-dir --eslint --no-git

プロジェクト作成後、確認のため package.json の内容を表示してください。
```

### 3. 必要なパッケージのインストール

```
以下のパッケージをインストールしてください：

npm install @anthropic-ai/sdk

これはClaude APIを使用するためのSDKです。
インストール完了後、package.jsonを確認してください。
```

### 4. 環境変数ファイルの作成

```
.env.local ファイルを作成してください。

以下の内容を記述：
ANTHROPIC_API_KEY=

このファイルは機密情報を含むため、.gitignoreに含まれていることを確認してください。
```

### 5. ディレクトリ構造の準備

```
以下のディレクトリ構造を作成してください：

src/
├── app/
│   ├── actions/         # Server Actions
│   ├── components/      # Reactコンポーネント
│   ├── lib/            # ユーティリティ
│   └── types/          # 型定義
├── page.tsx
└── layout.tsx

各ディレクトリに空の.gitkeepファイルを作成してください。
```

## 確認事項

以下のファイル・ディレクトリが作成されていることを確認：

- ✅ `package.json` - Next.js 14以上
- ✅ `tsconfig.json` - TypeScript設定
- ✅ `tailwind.config.ts` - Tailwind CSS設定
- ✅ `.env.local` - 環境変数ファイル
- ✅ `src/app/actions/` - Server Actions用
- ✅ `src/app/components/` - コンポーネント用
- ✅ `src/app/lib/` - ユーティリティ用
- ✅ `src/app/types/` - 型定義用

## 開発サーバーの起動確認

```
開発サーバーを起動してください：

npm run dev

正常に起動することを確認後、Ctrl+Cで停止してください。
```

ブラウザで http://localhost:3000 にアクセスして、Next.jsの初期画面が表示されることを確認。

## トラブルシューティング

### Node.jsのバージョンが古い

```bash
# Node.jsのバージョン確認
node -v

# 18以上が必要
# nvmを使用している場合
nvm install 18
nvm use 18
```

### パッケージインストールエラー

```bash
# node_modulesとロックファイルを削除して再インストール
rm -rf node_modules package-lock.json
npm install
```

### ポートが使用中

```
開発サーバーが別のポートで起動するよう設定してください：

package.jsonのscriptsセクションを以下のように修正：
"dev": "next dev -p 3001"
```

## 環境変数の設定

APIキーを取得していない場合：

1. https://console.anthropic.com/ にアクセス
2. アカウント作成/ログイン
3. API Keys から新しいキーを作成
4. `.env.local` に設定

```env
ANTHROPIC_API_KEY=sk-ant-...
```

## 次のステップ

プロジェクトの基盤ができたら、次はClaude APIとの統合を実装します：

👉 [01-api-integration.md](./01-api-integration.md) - Claude API統合

---

**ヒント**:
- 環境変数は必ず `.env.local` に設定（`.env` ではない）
- APIキーは絶対にGitにコミットしない
- 完成例は `../completed-example/` で確認可能
