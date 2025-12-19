# Claude Code サンプル集

このディレクトリには、Claude Codeを使用したアプリケーション開発のサンプルが含まれています。

## Claude Codeとは

Claude Codeは、AnthropicのAIアシスタントClaudeと対話しながらコーディングできる公式CLIツールです。

### 主な機能

- **対話型コーディング**: 自然言語でコードの生成・修正・リファクタリングが可能
- **コンテキスト理解**: プロジェクト全体を理解し、適切なコードを提案
- **マルチファイル編集**: 複数のファイルを同時に編集可能
- **ターミナル統合**: コマンドラインから直接使用可能

### セットアップ

Claude Codeをまだインストールしていない場合は、[Getting Started](../docs/getting-started.md) を参照してください。

## サンプル一覧

### 初心者向け

#### 1. [hello-claude](./hello-claude)

**難易度**: ⭐☆☆☆☆

Claude Codeの基本的な使い方を学ぶためのサンプルです。

**作るもの**: シンプルなタスクリストアプリ（HTML/CSS/JavaScript）

**学べること**:
- Claude Codeの基本操作
- 効果的なプロンプティング
- ファイル操作の基本
- 段階的な開発プロセス

**構成**:
- `working-directory/`: 空のディレクトリ（ここで作業）
- `completed-example/`: 完成版コード（参考用）
- `prompts/`: 00〜02の手順書（プロンプト付き）

**所要時間**: 約30分

---

### 中級者向け

#### 2. [nextjs-chat-app](./nextjs-chat-app)

**難易度**: ⭐⭐⭐☆☆

Next.js 14（App Router）とClaude APIを使用したチャットアプリケーションを構築します。

- Next.js App Routerの活用
- Claude APIとの統合
- Server Actionsの実装
- ストリーミングレスポンスの実装
- Tailwind CSSでのスタイリング

**学べること**:
- モダンなNext.jsアプリケーション開発
- AI APIの統合方法
- TypeScriptでの型安全な開発
- サーバーコンポーネントとクライアントコンポーネントの使い分け

**所要時間**: 約2-3時間

**技術スタック**:
- Next.js 14
- React 18
- TypeScript
- Tailwind CSS
- Claude API

---

#### 3. [langgraph-agent](./langgraph-agent)

**難易度**: ⭐⭐⭐⭐☆

LangGraphを使用して、複数のツールを使いこなすAIエージェントを作成します。

- LangGraphの基本概念
- ステートマシンの設計
- カスタムツールの作成
- エージェントのワークフロー設計
- FastAPIでのAPI化

**学べること**:
- LangGraphによるエージェント開発
- 複雑なワークフローの設計
- Pythonでのバックエンド開発
- AI駆動型アプリケーションのアーキテクチャ

**所要時間**: 約3-4時間

**技術スタック**:
- Python 3.10+
- LangGraph
- LangChain
- FastAPI
- Claude API

---

## 推奨する学習パス

### パス1: フロントエンド開発者向け

1. **hello-claude** - Claude Codeの基本を理解
2. **nextjs-chat-app** - Next.jsでのAI統合を学ぶ
3. **langgraph-agent** - バックエンドとの連携を学ぶ

### パス2: バックエンド開発者向け

1. **hello-claude** - Claude Codeの基本を理解
2. **langgraph-agent** - LangGraphでエージェントを作成
3. **nextjs-chat-app** - フロントエンドとの統合を学ぶ

### パス3: フルスタック開発者向け

1. **hello-claude** - 基本操作の習得
2. **nextjs-chat-app** と **langgraph-agent** を並行して学習
3. 両者を統合したフルスタックアプリケーションを構築

## Claude Code活用のコツ

### 効果的なプロンプトの書き方

1. **具体的に指示する**
   ```
   ❌ チャット機能を作って
   ✅ Next.js App Routerを使用して、メッセージ送信フォームと
      メッセージ履歴を表示するチャット画面を作成してください。
      Tailwind CSSでスタイリングしてください。
   ```

2. **コンテキストを提供する**
   ```
   現在のプロジェクト構成：
   - Next.js 14 (App Router)
   - TypeScript
   - Tailwind CSS

   以下の機能を追加してください：
   [機能の説明]
   ```

3. **段階的に進める**
   - 一度にすべてを実装しようとしない
   - 小さな機能から始めて、徐々に拡張する
   - 各ステップで動作確認を行う

### よくあるパターン

#### パターン1: 新規コンポーネントの作成

```
app/components/ui/配下に、以下の仕様でButtonコンポーネントを作成してください：

- TypeScriptで型定義
- variant プロパティ（primary, secondary, outline）
- size プロパティ（sm, md, lg）
- disabled state
- Tailwind CSSでスタイリング
- クリックイベントのハンドリング
```

#### パターン2: API統合

```
Claude APIを呼び出すServer Actionを実装してください：

ファイル: app/actions/chat.ts
要件:
- メッセージを受け取り、Claude APIに送信
- ストリーミングレスポンスに対応
- エラーハンドリング
- 環境変数からAPIキーを読み込み
```

#### パターン3: リファクタリング

```
以下のコンポーネントをリファクタリングしてください：

[コード]

改善点：
- カスタムフックに状態管理を移動
- メモ化を追加してパフォーマンス改善
- 型定義を別ファイルに分離
```

## トラブルシューティング

### Claude Codeが反応しない

```bash
# プロセスを確認
ps aux | grep claude

# キャッシュをクリア
claude cache clear

# 再起動
claude restart
```

### コード生成がうまくいかない

- プロンプトをより具体的にする
- 小さなタスクに分割する
- 既存のコードをコンテキストとして提供する
- エラーメッセージを共有する

### パフォーマンスが遅い

- 不要なファイルを`.claudeignore`に追加
- プロジェクトのサイズを最適化
- 必要なファイルだけをコンテキストに含める

## さらなる学習リソース

### 公式ドキュメント

- [Claude Code Documentation](https://docs.anthropic.com/claude/docs)
- [Claude API Reference](https://docs.anthropic.com/claude/reference)

### コミュニティ

- [Claude Code GitHub](https://github.com/anthropics/claude-code)
- [Discord Community](https://discord.gg/anthropic)

### 関連ツール

- [LangChain](https://langchain.com/)
- [LangGraph](https://langchain-ai.github.io/langgraph/)
- [Next.js](https://nextjs.org/)

## フィードバック

サンプルについての質問や改善提案は、[Issues](https://github.com/p0x0q/ai-agent-coding-hands-on/issues) で受け付けています。

新しいサンプルのアイデアも大歓迎です！

---

Happy Coding with Claude! 🚀
