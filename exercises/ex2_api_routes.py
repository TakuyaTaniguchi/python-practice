"""
演習2: FastAPIのルート定義

この演習では、FastAPIを使用してREST APIのエンドポイントを作成します。
Ruby on Railsのコントローラーに相当する機能を学びましょう。
"""

from fastapi import FastAPI, HTTPException, status
from typing import List
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


# 問題2: 全てのTodoを取得するエンドポイントを実装してください
# パス: "/todos"
# メソッド: GET
# 戻り値: Todoのリスト（response_modelを使用）
# ヒント: response_modelパラメータを使用してください
# TODO: ここにget_todos関数を実装


# 問題3: IDでTodoを取得するエンドポイントを実装してください
# パス: "/todos/{todo_id}"
# メソッド: GET
# パラメータ: todo_id (UUID型)
# 戻り値: 見つかったTodo、または404エラー
# ヒント: HTTPExceptionを使用してエラーを返す
# TODO: ここにget_todo関数を実装


# 問題4: 新しいTodoを作成するエンドポイントを実装してください
# パス: "/todos"
# メソッド: POST
# リクエストボディ: TodoCreate
# 戻り値: 作成されたTodo（201ステータスコード）
# ヒント: status_codeパラメータを使用してください
# TODO: ここにcreate_todo関数を実装


# 問題5: Todoを更新するエンドポイントを実装してください
# パス: "/todos/{todo_id}"
# メソッド: PUT
# パラメータ: todo_id (UUID型)
# リクエストボディ: TodoCreate
# 戻り値: 更新されたTodo、または404エラー
# TODO: ここにupdate_todo関数を実装


# 問題6: Todoを削除するエンドポイントを実装してください
# パス: "/todos/{todo_id}"
# メソッド: DELETE
# パラメータ: todo_id (UUID型)
# 戻り値: なし（204ステータスコード）、または404エラー
# TODO: ここにdelete_todo関数を実装