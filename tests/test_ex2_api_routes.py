"""
演習2のテスト: FastAPIルートのテスト
"""

import pytest
import sys
import os
from fastapi.testclient import TestClient
from uuid import UUID

# テスト対象のモジュールを追加
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from exercises.ex2_api_routes import app

client = TestClient(app)


def test_root_endpoint():
    """ルートエンドポイントが正しく実装されているかテスト"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the ToDo API"}


def test_get_todos_empty():
    """空のTodoリストを取得するエンドポイントが正しく実装されているかテスト"""
    # テスト前にTodoリストをクリア
    from exercises.ex2_api_routes import todos
    todos.clear()
    
    response = client.get("/todos")
    assert response.status_code == 200
    assert response.json() == []


def test_create_todo():
    """Todoを作成するエンドポイントが正しく実装されているかテスト"""
    # テスト前にTodoリストをクリア
    from exercises.ex2_api_routes import todos
    todos.clear()
    
    todo_data = {
        "title": "Test Todo",
        "description": "This is a test",
        "priority": "high",
        "completed": False
    }
    
    response = client.post("/todos", json=todo_data)
    assert response.status_code == 201
    
    data = response.json()
    assert data["title"] == "Test Todo"
    assert data["description"] == "This is a test"
    assert data["priority"] == "high"
    assert data["completed"] is False
    assert "id" in data
    
    # IDを保存して後のテストで使用
    return data["id"]


def test_get_todos_with_items():
    """Todoがある場合のリスト取得エンドポイントが正しく実装されているかテスト"""
    # テスト前にTodoリストをクリア
    from exercises.ex2_api_routes import todos
    todos.clear()
    
    # Todoを作成
    todo_id = test_create_todo()
    
    response = client.get("/todos")
    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["id"] == todo_id


def test_get_todo_by_id():
    """IDでTodoを取得するエンドポイントが正しく実装されているかテスト"""
    # Todoを作成してIDを取得
    todo_id = test_create_todo()
    
    response = client.get(f"/todos/{todo_id}")
    assert response.status_code == 200
    assert response.json()["id"] == todo_id
    assert response.json()["title"] == "Test Todo"


def test_get_todo_not_found():
    """存在しないIDでTodoを取得した場合のエラー処理が正しく実装されているかテスト"""
    response = client.get("/todos/00000000-0000-0000-0000-000000000000")
    assert response.status_code == 404
    assert "not found" in response.json()["detail"].lower()


def test_update_todo():
    """Todoを更新するエンドポイントが正しく実装されているかテスト"""
    # Todoを作成してIDを取得
    todo_id = test_create_todo()
    
    update_data = {
        "title": "Updated Todo",
        "description": "This todo has been updated",
        "priority": "low",
        "completed": True
    }
    
    response = client.put(f"/todos/{todo_id}", json=update_data)
    assert response.status_code == 200
    
    data = response.json()
    assert data["id"] == todo_id
    assert data["title"] == "Updated Todo"
    assert data["description"] == "This todo has been updated"
    assert data["priority"] == "low"
    assert data["completed"] is True


def test_delete_todo():
    """Todoを削除するエンドポイントが正しく実装されているかテスト"""
    # Todoを作成してIDを取得
    todo_id = test_create_todo()
    
    response = client.delete(f"/todos/{todo_id}")
    assert response.status_code == 204
    
    # 削除されたことを確認
    response = client.get(f"/todos/{todo_id}")
    assert response.status_code == 404


if __name__ == "__main__":
    # pytest.mainを使ってテストを実行
    pytest.main(["-v", __file__])