# Next.js Chat App - Claude APIを使ったチャットアプリケーション

このサンプルでは、Next.js 14（App Router）とClaude APIを使用して、モダンなAIチャットアプリケーションを構築します。

## 学習目標

- Next.js App Routerの理解と活用
- Claude APIとの統合方法
- Server Actionsの実装
- ストリーミングレスポンスの実装
- TypeScriptでの型安全な開発
- サーバーコンポーネントとクライアントコンポーネントの使い分け

## 前提条件

- Node.js v18以上
- Claude Codeがインストールされていること
- Anthropic APIキー（[公式サイト](https://console.anthropic.com/)で取得）
- React/Next.jsの基礎知識

## 難易度

⭐⭐⭐☆☆ 中級

## 所要時間

約2-3時間

## 完成イメージ

このサンプルを完成させると、以下の機能を持つチャットアプリができます：

- リアルタイムでClaudeと会話
- ストリーミングレスポンス（文字が流れるように表示）
- メッセージ履歴の管理
- マークダウンのレンダリング
- コードブロックのシンタックスハイライト
- レスポンシブデザイン

## 技術スタック

- **Next.js 14**: App Router
- **React 18**: Server/Client Components
- **TypeScript**: 型安全な開発
- **Tailwind CSS**: スタイリング
- **Anthropic SDK**: Claude APIクライアント
- **react-markdown**: マークダウンレンダリング

## ディレクトリ構成

```
nextjs-chat-app/
├── app/                          # Next.jsアプリケーション
│   ├── actions/                 # Server Actions
│   │   └── chat.ts             # Claude API呼び出し
│   ├── components/              # Reactコンポーネント
│   │   ├── ChatMessage.tsx     # メッセージ表示
│   │   ├── ChatInput.tsx       # 入力フォーム
│   │   └── ChatContainer.tsx   # チャット全体
│   ├── lib/                     # ユーティリティ
│   │   └── anthropic.ts        # Anthropicクライアント設定
│   ├── types/                   # 型定義
│   │   └── chat.ts             # チャット関連の型
│   ├── page.tsx                 # メインページ
│   └── layout.tsx               # ルートレイアウト
├── prompts/                      # プロンプト・手順書
│   ├── 01-setup.md              # プロジェクトセットアップ
│   ├── 02-api-integration.md    # API統合
│   ├── 03-streaming.md          # ストリーミング実装
│   ├── 04-ui-enhancement.md     # UI改善
│   └── prompts.json             # 再利用可能なプロンプト
└── README.md                     # このファイル
```

## 進め方

### ステップ1: 環境構築

1. このディレクトリに移動
   ```bash
   cd claude-code/nextjs-chat-app
   ```

2. プロンプトに従ってプロジェクトをセットアップ
   👉 [prompts/01-setup.md](./prompts/01-setup.md)

### ステップ2: Claude API統合

3. Claude APIとの連携を実装
   👉 [prompts/02-api-integration.md](./prompts/02-api-integration.md)

### ステップ3: ストリーミング実装

4. リアルタイムストリーミング機能を追加
   👉 [prompts/03-streaming.md](./prompts/03-streaming.md)

### ステップ4: UI改善

5. マークダウン対応とスタイル改善
   👉 [prompts/04-ui-enhancement.md](./prompts/04-ui-enhancement.md)

## 学べるポイント

### 1. Next.js App Routerの理解

- Server ComponentsとClient Componentsの違い
- Server Actionsを使ったAPI呼び出し
- ストリーミングとSuspense

### 2. AI API統合

- Anthropic SDKの使い方
- 環境変数の安全な管理
- エラーハンドリング
- レート制限への対応

### 3. TypeScript活用

- 型定義の作成
- ジェネリクスの活用
- 型安全なAPI呼び出し

### 4. ストリーミング実装

- Server-Sent Events（SSE）
- ReadableStreamの活用
- フロントエンドでのストリーミング受信

### 5. UI/UX

- レスポンシブデザイン
- ローディング状態の管理
- マークダウンレンダリング
- シンタックスハイライト

## 環境変数の設定

`.env.local` ファイルを作成（セットアップ手順に含まれます）：

```env
ANTHROPIC_API_KEY=your_api_key_here
```

**重要**: `.env.local`は`.gitignore`に含まれているため、Gitにコミットされません。

## よくある質問

### Q: Next.js App Routerとは？

A: Next.js 13以降で導入された新しいルーティングシステムです。Server Componentsをデフォルトで使用し、より効率的なアプリケーションを構築できます。

### Q: Server ActionsとAPI Routesの違いは？

A: Server Actionsは、コンポーネントから直接サーバー側の関数を呼び出せる機能です。API Routesよりもシンプルに書けます。

### Q: ストリーミングのメリットは？

A: ユーザーは応答を待たずに、生成されたテキストをリアルタイムで見ることができます。UXが大幅に向上します。

### Q: TypeScriptは必須ですか？

A: 必須ではありませんが、大規模なアプリケーションでは型安全性が重要です。このサンプルで学ぶことをお勧めします。

## トラブルシューティング

### APIキーが認識されない

```bash
# .env.localファイルが正しい場所にあるか確認
ls -la .env.local

# 開発サーバーを再起動
pnpm dev
```

### ストリーミングが動かない

```
# Claude Codeに質問
現在のストリーミング実装で、テキストが流れるように表示されません。
考えられる原因と解決方法を教えてください。

関連コード：
[actions/chat.tsとコンポーネントのコードを貼り付け]
```

### ビルドエラー

```
# 型エラーの場合
pnpm tsc --noEmit

# 依存関係の問題の場合
rm -rf node_modules .next
pnpm install
```

## 応用課題

基本実装ができたら、以下に挑戦してみましょう：

### 1. 会話履歴の永続化

```
会話履歴をブラウザのLocalStorageに保存する機能を追加してください。
ページをリロードしても会話が残るようにします。
```

### 2. システムプロンプトのカスタマイズ

```
ユーザーがシステムプロンプトを設定できる機能を追加してください。
設定画面とLocalStorageでの保存を実装します。
```

### 3. マルチターン会話

```
現在の実装を拡張して、複数回のやり取りを
コンテキストとして保持する機能を実装してください。
```

### 4. ファイルアップロード

```
画像をアップロードして、Claude Visionで
分析できる機能を追加してください。
```

### 5. チャット履歴管理

```
複数のチャットセッションを作成・管理できる機能を追加してください。
- サイドバーでチャット一覧表示
- 新規チャット作成
- チャット削除
- チャット名の編集
```

### 6. データベース連携

```
Supabaseを使用して、会話履歴を
クラウドに保存する機能を実装してください。
```

## アーキテクチャのポイント

### Server Componentsの活用

```typescript
// page.tsx - Server Component
export default function ChatPage() {
  // サーバーでデータフェッチ可能
  return <ChatContainer />
}
```

### Client Componentsの使用

```typescript
// ChatInput.tsx - Client Component
'use client'

export function ChatInput() {
  // useStateなどのhooksが使える
  const [message, setMessage] = useState('')
  // ...
}
```

### Server Actions

```typescript
// actions/chat.ts
'use server'

export async function sendMessage(message: string) {
  // サーバーサイドで実行される
  const response = await anthropic.messages.create({...})
  return response
}
```

## パフォーマンス最適化

実装が完成したら、以下を確認：

1. **不要な再レンダリング**
   - React.memoの使用
   - useCallbackでコールバックをメモ化

2. **バンドルサイズ**
   - 動的インポートの活用
   - 不要な依存関係の削除

3. **ネットワーク**
   - ストリーミングの最適化
   - エラーリトライの実装

## セキュリティチェックリスト

- ✅ APIキーが環境変数に保存されている
- ✅ クライアント側にAPIキーが露出していない
- ✅ ユーザー入力のバリデーション
- ✅ レート制限の実装
- ✅ エラーメッセージに機密情報が含まれていない

## 次のステップ

このサンプルを完了したら：

1. [langgraph-agent](../langgraph-agent) - バックエンドでのAIエージェント実装
2. 両方を統合してフルスタックアプリケーションを構築
3. [best-practices.md](../../docs/best-practices.md) で開発のベストプラクティスを確認

## 参考リソース

- [Next.js App Router](https://nextjs.org/docs/app)
- [Anthropic API Documentation](https://docs.anthropic.com/)
- [React Server Components](https://react.dev/blog/2023/03/22/react-labs-what-we-have-been-working-on-march-2023#react-server-components)
- [Tailwind CSS](https://tailwindcss.com/)

---

質問や問題があれば、[Issues](https://github.com/yourusername/ai-agent-coding-hands-on/issues)で報告してください！
