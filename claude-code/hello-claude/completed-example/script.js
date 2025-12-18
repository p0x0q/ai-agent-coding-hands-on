// 定数定義
const STORAGE_KEY = 'tasks';
const MAX_TASK_LENGTH = 200;

// DOM要素の取得
const taskInput = document.getElementById('taskInput');
const addButton = document.getElementById('addButton');
const taskList = document.getElementById('taskList');

// タスクデータを保持する配列
let tasks = [];

/**
 * 初期化処理
 */
function init() {
    // LocalStorageからタスクを読み込む
    loadTasks();

    // イベントリスナーの設定
    addButton.addEventListener('click', handleAddTask);
    taskInput.addEventListener('keypress', handleKeyPress);

    // タスクリストを表示
    renderTasks();
}

/**
 * タスクを追加する
 */
function handleAddTask() {
    const taskText = taskInput.value.trim();

    // 入力値の検証
    if (!taskText) {
        return;
    }

    if (taskText.length > MAX_TASK_LENGTH) {
        alert(`タスクは${MAX_TASK_LENGTH}文字以内で入力してください`);
        return;
    }

    // タスクオブジェクトを作成
    const task = {
        id: Date.now(),
        text: taskText,
        completed: false,
        createdAt: new Date().toISOString()
    };

    // タスクを配列に追加
    tasks.push(task);

    // LocalStorageに保存
    saveTasks();

    // 表示を更新
    renderTasks();

    // 入力フィールドをクリア
    taskInput.value = '';
    taskInput.focus();
}

/**
 * Enterキー押下時の処理
 */
function handleKeyPress(event) {
    if (event.key === 'Enter') {
        handleAddTask();
    }
}

/**
 * タスクを削除する
 */
function deleteTask(taskId) {
    tasks = tasks.filter(task => task.id !== taskId);
    saveTasks();
    renderTasks();
}

/**
 * タスクの完了状態を切り替える
 */
function toggleTaskComplete(taskId) {
    const task = tasks.find(t => t.id === taskId);
    if (task) {
        task.completed = !task.completed;
        saveTasks();
        renderTasks();
    }
}

/**
 * タスクリストを表示する
 */
function renderTasks() {
    // リストをクリア
    taskList.innerHTML = '';

    // タスクがない場合
    if (tasks.length === 0) {
        const emptyState = document.createElement('div');
        emptyState.className = 'empty-state';
        emptyState.textContent = 'タスクがありません。新しいタスクを追加しましょう！';
        taskList.appendChild(emptyState);
        return;
    }

    // 各タスクを表示
    tasks.forEach(task => {
        const li = createTaskElement(task);
        taskList.appendChild(li);
    });
}

/**
 * タスク要素を作成する
 */
function createTaskElement(task) {
    const li = document.createElement('li');
    li.className = 'task-item';
    if (task.completed) {
        li.classList.add('completed');
    }

    // チェックボックス
    const checkbox = document.createElement('input');
    checkbox.type = 'checkbox';
    checkbox.className = 'task-checkbox';
    checkbox.checked = task.completed;
    checkbox.addEventListener('change', () => toggleTaskComplete(task.id));

    // タスクテキスト
    const taskText = document.createElement('span');
    taskText.className = 'task-text';
    taskText.textContent = task.text;

    // 削除ボタン
    const deleteBtn = document.createElement('button');
    deleteBtn.className = 'delete-btn';
    deleteBtn.textContent = '削除';
    deleteBtn.addEventListener('click', () => {
        if (confirm('このタスクを削除しますか？')) {
            deleteTask(task.id);
        }
    });

    // 要素を組み立て
    li.appendChild(checkbox);
    li.appendChild(taskText);
    li.appendChild(deleteBtn);

    return li;
}

/**
 * LocalStorageにタスクを保存する
 */
function saveTasks() {
    try {
        localStorage.setItem(STORAGE_KEY, JSON.stringify(tasks));
    } catch (error) {
        console.error('タスクの保存に失敗しました:', error);
        alert('タスクの保存に失敗しました。ストレージがいっぱいの可能性があります。');
    }
}

/**
 * LocalStorageからタスクを読み込む
 */
function loadTasks() {
    try {
        const stored = localStorage.getItem(STORAGE_KEY);
        if (stored) {
            tasks = JSON.parse(stored);
        }
    } catch (error) {
        console.error('タスクの読み込みに失敗しました:', error);
        tasks = [];
    }
}

/**
 * デバッグ用：LocalStorageをクリア
 * 開発者コンソールから clearStorage() で実行可能
 */
function clearStorage() {
    localStorage.removeItem(STORAGE_KEY);
    tasks = [];
    renderTasks();
    console.log('ストレージをクリアしました');
}

// ページ読み込み時に初期化
init();
