"""
演習1のテスト: Pydanticモデルのテスト
"""

import pytest
import sys
import os

# テスト対象のモジュールを追加
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from exercises.ex1_basic_models import Priority, TodoCreate, Todo


def test_priority_enum():
    """Priority Enumが正しく実装されているかテスト"""
    # Enumの値が存在するか確認
    assert hasattr(Priority, 'LOW')
    assert hasattr(Priority, 'MEDIUM')
    assert hasattr(Priority, 'HIGH')
    
    # 値が文字列型であることを確認
    assert Priority.LOW.value == "low"
    assert Priority.MEDIUM.value == "medium"
    assert Priority.HIGH.value == "high"
    
    # Enumの比較が正しく動作することを確認
    assert Priority.LOW == Priority.LOW
    assert Priority.LOW != Priority.MEDIUM


def test_todo_create_model():
    """TodoCreateモデルが正しく実装されているかテスト"""
    # 必須フィールドのみで作成
    todo = TodoCreate(title="Test Todo")
    assert todo.title == "Test Todo"
    assert todo.description is None
    assert todo.priority == Priority.MEDIUM
    assert todo.completed is False
    
    # 全フィールド指定で作成
    todo = TodoCreate(
        title="Complete Task",
        description="This is a test task",
        priority=Priority.HIGH,
        completed=True
    )
    assert todo.title == "Complete Task"
    assert todo.description == "This is a test task"
    assert todo.priority == Priority.HIGH
    assert todo.completed is True
    
    # dictへの変換テスト
    todo_dict = todo.dict()
    assert todo_dict["title"] == "Complete Task"
    assert todo_dict["priority"] == Priority.HIGH


def test_todo_model():
    """Todoモデルが正しく実装されているかテスト"""
    # Todoモデルがidフィールドを持つことを確認
    todo = Todo(
        id="123e4567-e89b-12d3-a456-426614174000",
        title="Test Todo",
        description="This is a test",
        priority=Priority.LOW,
        completed=False
    )
    assert todo.id == "123e4567-e89b-12d3-a456-426614174000"
    assert todo.title == "Test Todo"
    assert todo.description == "This is a test"
    assert todo.priority == Priority.LOW
    assert todo.completed is False
    
    # TodoCreateからの継承を確認（TodoCreateのフィールドが全て含まれるか）
    assert all(field in todo.dict() for field in [
        "id", "title", "description", "priority", "completed"
    ])


if __name__ == "__main__":
    # pytest.mainを使ってテストを実行
    pytest.main(["-v", __file__])