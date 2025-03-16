"""
演習2: FastAPIのルート定義

この演習では、FastAPIを使用してREST APIのエンドポイントを作成します。
Ruby on Railsのコントローラーに相当する機能を学びましょう。
"""

from fastapi import FastAPI, HTTPException, status,Query
from typing import List,Annotated
from uuid import uuid4, UUID

# 演習1で作成したモデルをインポート
# 実際の回答時にはこのパスを変更する必要があるかもしれません
from exercises.ex1_basic_models import Todo, TodoCreate, Priority

app = FastAPI()

# インメモリデータベース
todos = []

# 問題1: ルートパス("/")へのGETリクエストを処理する関数を実装してください
# 戻り値: {"message": "Welcome to the ToDo API"}
# ヒント: @app.get デコレータを使用します
# TODO: ここにroot関数を実装

@app.get("/")
def root():
    return  {"message": "Welcome to the ToDo API"}

# 問題2: 全てのTodoを取得するエンドポイントを実装してください
# パス: "/todos"
# メソッド: GET
# 戻り値: Todoのリスト（response_modelを使用）
# ヒント: response_modelパラメータを使用してください
# TODO: ここにget_todos関数を実装

@app.get("/todos",response_model=List[Todo])
def get_todos():
    return todos



# 問題3: IDでTodoを取得するエンドポイントを実装してください
# パス: "/todos/{response_model=Item,}"
# メソッド: GET
# パラメータ: todo_id (UUID型)
# 戻り値: 見つかったTodo、または404エラー
# ヒント: HTTPExceptionを使用してエラーを返す
# TODO: ここにget_todo関数を実装

@app.get("/todos/{todo_id}",response_model=Todo)
def get_todo(todo_id: UUID):
    result = []
    for todo in todos:
        if todo.id == todo_id:
            result.append(todo)
    if result:
        return result
    else:
        raise HTTPException(status_code=404, detail="Item not found")

# 問題4: 新しいTodoを作成するエンドポイントを実装してください
# パス: "/todos"
# メソッド: POST
# リクエストボディ: TodoCreate
# 戻り値: 作成されたTodo（201ステータスコード）
# ヒント: status_codeパラメータを使用してください
# TODO: ここにcreate_todo関数を実装

@app.post("/todos",response_model=Todo,status_code=201)
def create_todo(todo: TodoCreate):
    new_todo = Todo(id=str(uuid4()),**dict(todo))
    todos.append(new_todo)
    HTTPException(status_code=201, detail="Item not found")
    return new_todo



# 問題5: Todoを更新するエンドポイントを実装してください
# パス: "/todos/{todo_id}"
# メソッド: PUT
# パラメータ: todo_id (UUID型)
# リクエストボディ: TodoCreate
# 戻り値: 更新されたTodo、または404エラー
# TODO: ここにupdate_todo関数を実装

@app.put("/todos/{todo_id}",response_model=Todo)
def update_todo(todo_id: UUID, todo_update: TodoCreate):

    for index,todo in enumerate(todos):
        if todo.id == todo_id:
            updated_todo = Todo(id=str(todo_id), **todo_update.dict())
            todos[index] = updated_todo
            return updated_todo
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Todo with ID {todo_id} not found"
    )

# 問題6: Todoを削除するエンドポイントを実装してください
# パス: "/todos/{todo_id}"
# メソッド: DELETE
# パラメータ: todo_id (UUID型)
# 戻り値: なし（204ステータスコード）、または404エラー
# TODO: ここにdelete_todo関数を実装

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



