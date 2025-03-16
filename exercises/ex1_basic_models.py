"""
演習1: 基本的なPydanticモデルの作成

この演習では、FastAPIで使用するPydanticモデルを作成します。
TypeScriptのinterfaceやtypeに相当するものを学びましょう。
"""

from pydantic import BaseModel
from typing import Optional
from enum import Enum

# 問題1: 優先度を表すEnumを作成してください
# 以下の3つの値を持つenumを定義: LOW, MEDIUM, HIGH
# ヒント: Python の enum.Enum クラスを継承します
# TODO: ここにPriorityクラスを実装

class Priority(Enum):
    LOW = 'low'
    MEDIUM = 'medium'
    HIGH = 'high'

# 問題2: TodoCreateモデルを作成してください
# 以下のフィールドが必要です:
# - title: 文字列（必須）
# - description: 文字列（任意、デフォルトはNone）
# - priority: Priority enum（デフォルトはMEDIUM）
# - completed: 真偽値（デフォルトはFalse）
# ヒント: BaseModelを継承します
# TODO: ここにTodoCreateクラスを実装

class TodoCreate(BaseModel):
    title: str
    description: str = None
    priority: Priority = Priority.MEDIUM
    completed: bool = False

# 問題3: TodoモデルをTodoCreateを継承して作成してください
# TodoCreateの全フィールドに加えて、以下のフィールドが必要:
# - id: 文字列（必須）
# ヒント: TodoCreateを継承します
# TODO: ここにTodoクラスを実装

class Todo(TodoCreate):
    id: str