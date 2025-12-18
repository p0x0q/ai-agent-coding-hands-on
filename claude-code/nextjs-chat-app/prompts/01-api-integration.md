# ステップ1: Claude API統合

このステップでは、Claude APIとの連携を実装します。

## 学習ポイント

- Anthropic SDKの使用方法
- Server Actionsの実装
- 型定義の作成
- エラーハンドリング

## 実行手順

### 1. 型定義の作成

```
src/app/types/chat.ts を作成してください。

以下の型を定義：

export interface Message {
  role: 'user' | 'assistant';
  content: string;
  id: string;
  timestamp: number;
}

export interface ChatResponse {
  success: boolean;
  message?: string;
  error?: string;
}
```

### 2. Anthropicクライアントの設定

```
src/app/lib/anthropic.ts を作成してください。

要件：
- Anthropic SDKをインポート
- 環境変数からAPIキーを読み込み
- Anthropicクライアントのインスタンスを作成・エクスポート
- APIキーが設定されていない場合のエラーハンドリング

例：
import Anthropic from '@anthropic-ai/sdk';

if (!process.env.ANTHROPIC_API_KEY) {
  throw new Error('ANTHROPIC_API_KEY is not set');
}

export const anthropic = new Anthropic({
  apiKey: process.env.ANTHROPIC_API_KEY,
});
```

### 3. Server Actionの実装

```
src/app/actions/chat.ts を作成してください。

Server Actionとして、以下の関数を実装：

関数名: sendMessage
パラメータ:
  - message: string (ユーザーのメッセージ)
  - history: Message[] (会話履歴、オプション)
戻り値: Promise<ChatResponse>

処理内容：
1. 'use server' ディレクティブを追加
2. anthropicクライアントを使用してClaude APIを呼び出し
3. モデル: 'claude-3-5-sonnet-20241022'
4. max_tokens: 1024
5. メッセージ履歴を考慮した会話
6. エラーハンドリングを実装
7. レスポンスを返す

コメントを付けて実装してください。
```

## 確認事項

### ファイルが作成されていることを確認

- ✅ `src/app/types/chat.ts`
- ✅ `src/app/lib/anthropic.ts`
- ✅ `src/app/actions/chat.ts`

### 型チェック

```bash
npm run build

# エラーがないことを確認
```

## テスト

### Server Actionのテスト

一時的なテストページを作成してServer Actionが動作することを確認：

```
src/app/test/page.tsx を作成してください。

簡単なフォームを作成：
- テキスト入力
- 送信ボタン
- レスポンス表示エリア

sendMessage Server Actionを呼び出して動作を確認してください。
```

http://localhost:3000/test にアクセスして動作確認。

## トラブルシューティング

### APIキーエラー

```.env.local ファイルを確認してください：

ANTHROPIC_API_KEY が正しく設定されているか
開発サーバーを再起動（環境変数の読み込みのため）
```

### TypeScriptエラー

```
型定義を確認してください。
以下のコマンドで型チェック：

npx tsc --noEmit
```

### Server Actionが動かない

```
'use server' ディレクティブがファイルの先頭にあるか確認
関数がasyncであることを確認
エクスポートされているか確認
```

## プロンプトの例

### 基本的なテスト

```
こんにちは
```

期待されるレスポンス：Claudeからの挨拶

### 会話の継続

```
履歴を含めてメッセージを送信し、文脈が保持されるか確認
```

## コードの確認ポイント

### Server Action (chat.ts)

```typescript
'use server'

import { anthropic } from '@/lib/anthropic'
import { Message, ChatResponse } from '@/types/chat'

export async function sendMessage(
  message: string,
  history: Message[] = []
): Promise<ChatResponse> {
  try {
    // メッセージ履歴を Anthropic API形式に変換
    const messages = [
      ...history.map(msg => ({
        role: msg.role,
        content: msg.content
      })),
      {
        role: 'user' as const,
        content: message
      }
    ]

    // Claude API呼び出し
    const response = await anthropic.messages.create({
      model: 'claude-3-5-sonnet-20241022',
      max_tokens: 1024,
      messages
    })

    // レスポンスの取得
    const content = response.content[0]
    if (content.type !== 'text') {
      throw new Error('Unexpected response type')
    }

    return {
      success: true,
      message: content.text
    }
  } catch (error) {
    console.error('Error calling Claude API:', error)
    return {
      success: false,
      error: error instanceof Error ? error.message : 'Unknown error'
    }
  }
}
```

## 次のステップ

Claude APIとの基本的な統合ができたら、次はストリーミング機能を実装します：

👉 [02-streaming.md](./02-streaming.md) - ストリーミング実装

---

**ヒント**:
- Server Actionsはサーバーサイドでのみ実行される
- 環境変数はサーバーサイドでのみアクセス可能
- 完成例でコードの詳細を確認できます
