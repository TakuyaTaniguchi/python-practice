# Python実践学習演習

このリポジトリには、TypeScriptやRuby on Rails経験者がPythonとFastAPIを学ぶための実践的な演習問題が含まれています。各演習は穴埋め形式になっており、コメントで記述された問題に沿ってコードを完成させることで、Pythonの基本からFastAPIの機能まで幅広く学習できます。

## 演習の内容

1. **演習1: Pydanticモデルの作成**
   - TypeScriptのinterfaceやtypeに相当する機能を学ぶ
   - ファイル: `exercises/ex1_basic_models.py`
   - テスト: `tests/test_ex1_models.py`

2. **演習2: FastAPIのルート定義**
   - Ruby on Railsのコントローラーに相当する機能を学ぶ
   - ファイル: `exercises/ex2_api_routes.py`
   - テスト: `tests/test_ex2_api_routes.py`

3. **演習3: 非同期操作の実装**
   - Pythonの非同期処理（async/await）を学ぶ
   - ファイル: `exercises/ex3_async_operations.py`
   - テスト: `tests/test_ex3_async.py`

4. **演習4: Python基本文法演習**
   - リスト・辞書操作、可変性と参照、関数の高度な機能など
   - TypeScriptやRubyから入った人が躓きやすいポイントを学ぶ
   - ファイル: `exercises/ex4_python_basics.py`
   - テスト: `tests/test_ex4_python_basics.py`

## 演習の進め方

1. 各演習ファイル（`exercises/`ディレクトリ内）を開き、コメントで指示されている内容に従ってコードを実装してください
2. `TODO`コメントが書かれている場所に必要なコードを追加します
3. テストを実行して実装が正しいか確認します

## テストの実行方法

各演習のテストを実行するには、以下のコマンドを使用します：

```bash
# 事前準備（初回のみ）
pip install pytest pytest-asyncio

# 個別のテストを実行
python tests/test_ex1_models.py
python tests/test_ex2_api_routes.py
python tests/test_ex3_async.py
python tests/test_ex4_python_basics.py

# または全テストを一度に実行
pytest
```

## 学習のヒント

- テストコードを読むことで、実装すべき内容の詳細がわかります
- エラーメッセージをよく読んで、何が間違っているかを理解しましょう
- 各演習ファイルには、コメントでヒントが記載されています
- [LEARNING_GUIDE.md](LEARNING_GUIDE.md)に、より詳細な学習ポイントが記載されています

## 解答例

各演習の解答例は以下のようになります（実際に自分で考えて実装する前に見ないでください）：

<details>
<summary>演習1の解答例</summary>

```python
# 問題1: 優先度を表すEnumを作成してください
class Priority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

# 問題2: TodoCreateモデルを作成してください
class TodoCreate(BaseModel):
    title: str
    description: Optional[str] = None
    priority: Priority = Priority.MEDIUM
    completed: bool = False

# 問題3: TodoモデルをTodoCreateを継承して作成してください
class Todo(TodoCreate):
    id: str
```
</details>

<details>
<summary>演習2の解答例</summary>

```python
# 問題1: ルートパスへのGETリクエストを処理する関数
@app.get("/")
async def root():
    return {"message": "Welcome to the ToDo API"}

# 問題2: 全てのTodoを取得するエンドポイント
@app.get("/todos", response_model=List[Todo])
async def get_todos():
    return todos

# 問題3: IDでTodoを取得するエンドポイント
@app.get("/todos/{todo_id}", response_model=Todo)
async def get_todo(todo_id: UUID):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Todo with ID {todo_id} not found"
    )

# 問題4: 新しいTodoを作成するエンドポイント
@app.post("/todos", response_model=Todo, status_code=status.HTTP_201_CREATED)
async def create_todo(todo: TodoCreate):
    new_todo = Todo(id=str(uuid4()), **todo.dict())
    todos.append(new_todo)
    return new_todo

# 問題5: Todoを更新するエンドポイント
@app.put("/todos/{todo_id}", response_model=Todo)
async def update_todo(todo_id: UUID, todo_update: TodoCreate):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            updated_todo = Todo(id=str(todo_id), **todo_update.dict())
            todos[index] = updated_todo
            return updated_todo
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Todo with ID {todo_id} not found"
    )

# 問題6: Todoを削除するエンドポイント
@app.delete("/todos/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(todo_id: UUID):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos.pop(index)
            return
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Todo with ID {todo_id} not found"
    )
```
</details>

<details>
<summary>演習3の解答例</summary>

```python
# 問題1: 非同期関数
async def async_wait(seconds: float) -> float:
    await asyncio.sleep(seconds)
    return seconds

# 問題2: 複数の非同期処理を並行実行する関数
async def run_parallel(wait_times: List[float]) -> List[tuple]:
    async def measure_time(wait_time: float) -> tuple:
        start_time = time.time()
        await async_wait(wait_time)
        actual_time = time.time() - start_time
        return (wait_time, actual_time)
    
    tasks = [measure_time(wait_time) for wait_time in wait_times]
    return await asyncio.gather(*tasks)

# 問題3: 非同期ジェネレータ関数
async def async_counter(count: int, interval: float):
    for i in range(count):
        yield i
        await asyncio.sleep(interval)

# 問題4: 非同期コンテキストマネージャ
class AsyncTimer:
    async def __aenter__(self):
        self.start_time = time.time()
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        self.elapsed = time.time() - self.start_time
        print(f"Elapsed time: {self.elapsed:.4f} seconds")
    
    def __float__(self):
        return self.elapsed
        
    def __gt__(self, other):
        return float(self) > other
        
    def __lt__(self, other):
        return float(self) < other
```
</details>

<details>
<summary>演習4の解答例</summary>

```python
# 問題1: リスト操作関数
def list_operations():
    # 元のリスト
    original = [1, 2, 3, 4, 5]
    
    # 問題1-1: スライスでリストの最初の3要素を取得
    result1 = original[0:3]  # original[:3] でも可
    
    # 問題1-2: リストを逆順にする
    result2 = original[::-1]
    
    # 問題1-3: リスト内包表記で各要素を2倍にする
    result3 = [x * 2 for x in original]
    
    # 問題1-4: リストに要素を追加
    original.extend([6, 7, 8])
    result4 = original
    
    return (result1, result2, result3, result4)

# 問題2: 辞書操作関数
def dict_operations():
    # 元の辞書
    user = {
        "name": "Taro",
        "age": 30,
        "skills": ["Python", "JavaScript"]
    }
    
    # 問題2-1: 辞書から安全に値を取得
    result1 = user.get("email", "Not found")
    
    # 問題2-2: 辞書内包表記で各キーと値の長さを持つ辞書を作成
    result2 = {
        key: len(value) if isinstance(value, (str, list, tuple, dict)) else 1
        for key, value in user.items()
    }
    
    # 問題2-3: 辞書に要素を追加
    user["email"] = "taro@example.com"
    result3 = user
    
    # 問題2-4: 辞書のキーと値を入れ替え
    result4 = {value: key for key, value in user.items() if isinstance(value, str)}
    
    return (result1, result2, result3, result4)

# 問題3: 可変性と参照関数
def mutability_and_references():
    # 問題3-1: リストのコピー方法
    original = [1, 2, [3, 4]]
    shallow_copy = original.copy()
    import copy
    deep_copy = copy.deepcopy(original)
    
    original[2][0] = 99
    result1 = (original, shallow_copy, deep_copy)
    
    # 問題3-2: 可変デフォルト引数の問題
    def append_to_list(item, target_list=None):
        if target_list is None:
            target_list = []
        target_list.append(item)
        return target_list
    
    result2a = append_to_list(1)
    result2b = append_to_list(2)
    result2c = append_to_list(3)
    result2 = (result2a, result2b, result2c)
    
    # 問題3-3: 文字列連結とリスト連結の挙動
    def string_concatenation():
        s = "Hello"
        str_id_before = id(s)
        s += " World"
        str_id_after = id(s)
        
        lst = [1, 2, 3]
        list_id_before = id(lst)
        lst += [4, 5]
        list_id_after = id(lst)
        
        return (str_id_before, str_id_after, list_id_before, list_id_after)
    
    result3 = string_concatenation()
    
    return (result1, result2, result3)

# 問題4: 関数の高度な機能
def advanced_functions():
    # 問題4-1: ラムダ関数を使ったソート
    numbers = [1, 5, 2, 4, 3]
    result1 = sorted(numbers, key=lambda x: x**2)
    
    # 問題4-2: デコレータ関数
    def timing_decorator(func):
        def wrapper(*args, **kwargs):
            import time
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            execution_time = end_time - start_time
            return execution_time, result
        return wrapper
    
    @timing_decorator
    def slow_function():
        import time
        time.sleep(0.1)
        return "Done!"
    
    result2 = slow_function()
    
    # 問題4-3: 可変長引数と辞書型可変長引数
    def flexible_function(required_arg, *args, **kwargs):
        return required_arg, args, kwargs
    
    result3 = flexible_function("必須", 1, 2, 3, name="Taro", age=30)
    
    # 問題4-4: クロージャを使った関数ファクトリ
    def multiplier_factory(factor):
        def multiplier(x):
            return x * factor
        return multiplier
    
    double = multiplier_factory(2)
    triple = multiplier_factory(3)
    result4 = (double(5), triple(5))
    
    return (result1, result2, result3, result4)
```
</details>

## 発展課題

基本的な演習を完了したら、以下の発展課題に挑戦してみましょう：

1. 実際のデータベース（SQLite）を使用するように機能を拡張する
2. JWT認証を追加して保護されたエンドポイントを作成する
3. パス操作関数をルーターに分割して整理する
4. 非同期テストケースを書いてテストの coverage を向上させる

これらの課題について詳しく知りたい場合は、[LEARNING_GUIDE.md](LEARNING_GUIDE.md)の「次のステップ」セクションを参照してください。