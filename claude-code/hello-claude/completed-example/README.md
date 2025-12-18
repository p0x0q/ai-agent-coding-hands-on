# Hello Claude - 完成例

これは、promptsディレクトリの手順に従って実装した場合の完成形です。

## 機能

- ✅ タスクの追加
- ✅ タスクの削除
- ✅ タスクの完了/未完了の管理
- ✅ LocalStorageによるデータ永続化
- ✅ Enterキーでの追加
- ✅ レスポンシブデザイン
- ✅ ダークモード対応
- ✅ アクセシビリティ対応

## ファイル構成

```
completed-example/
├── index.html       # メインHTMLファイル
├── styles.css       # スタイルシート（レスポンシブ・ダークモード対応）
├── script.js        # JavaScript（全機能実装）
├── test.html        # 簡易テストページ
└── README.md        # このファイル
```

## 実行方法

### 1. ローカルサーバーで起動

```bash
# Pythonを使用
python3 -m http.server 8000

# または、Node.jsを使用
npx serve

# または、VS Code Live Serverを使用
右クリック > Open with Live Server
```

### 2. ブラウザで確認

```
http://localhost:8000
```

## 使い方

1. 入力フィールドにタスクを入力
2. 「追加」ボタンをクリック、またはEnterキーで追加
3. チェックボックスをクリックして完了/未完了を切り替え
4. 「削除」ボタンでタスクを削除

## テスト

`test.html`をブラウザで開くと、基本的な動作テストを実行できます。

## コードのポイント

### 1. 構造化された関数

- `init()`: 初期化処理
- `handleAddTask()`: タスク追加
- `deleteTask()`: タスク削除
- `toggleTaskComplete()`: 完了状態の切り替え
- `renderTasks()`: 表示更新
- `saveTasks()` / `loadTasks()`: データ永続化

### 2. エラーハンドリング

- 入力値の検証
- LocalStorageのエラーハンドリング
- 削除前の確認ダイアログ

### 3. アクセシビリティ

- セマンティックなHTML
- aria-label属性
- role属性

### 4. レスポンシブデザイン

- 768px以下でモバイル対応レイアウト
- フレキシブルな入力エリア

### 5. ダークモード

- `prefers-color-scheme: dark` メディアクエリ
- 自動的にシステム設定に対応

## カスタマイズ例

### タスクの最大文字数を変更

```javascript
// script.js
const MAX_TASK_LENGTH = 200; // この値を変更
```

### カラーテーマの変更

```css
/* styles.css */
#addButton {
    background-color: #4CAF50; /* この色を変更 */
}
```

### ストレージキーの変更

```javascript
// script.js
const STORAGE_KEY = 'tasks'; // この値を変更
```

## デバッグ

### LocalStorageをクリア

ブラウザの開発者コンソールで以下を実行：

```javascript
clearStorage()
```

### タスクデータの確認

```javascript
console.log(tasks)
```

## ブラウザ対応

- Chrome/Edge: 最新版
- Firefox: 最新版
- Safari: 最新版
- モバイルブラウザ: iOS Safari, Chrome for Android

## 学習ポイント

このコードから学べること：

1. **DOM操作の基本**
   - 要素の取得
   - イベントリスナーの設定
   - 動的な要素の作成

2. **データ管理**
   - 配列でのデータ保持
   - オブジェクトの設計
   - LocalStorageの活用

3. **関数設計**
   - 単一責任の原則
   - 再利用可能な関数
   - エラーハンドリング

4. **CSSの実践**
   - Flexboxレイアウト
   - トランジション効果
   - レスポンシブデザイン
   - ダークモード

## さらなる改善案

実装したい場合のアイデア：

1. タスクの編集機能
2. カテゴリ分類
3. 優先度設定
4. 期限設定
5. フィルター機能（全て/未完了/完了済み）
6. ソート機能
7. タスクの検索
8. データのエクスポート/インポート

## 参考リソース

- [MDN Web Docs - JavaScript](https://developer.mozilla.org/ja/docs/Web/JavaScript)
- [MDN Web Docs - LocalStorage](https://developer.mozilla.org/ja/docs/Web/API/Window/localStorage)
- [CSS Flexbox Guide](https://css-tricks.com/snippets/css/a-guide-to-flexbox/)
