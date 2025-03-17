"""
演習4のテスト: Python基本文法のテスト
"""

import pytest
import sys
import os
import time
import copy

# テスト対象のモジュールを追加
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from exercises.ex4_python_basics import list_operations, dict_operations, mutability_and_references, advanced_functions


def test_list_operations():
    """リスト操作関数のテスト"""
    result1, result2, result3, result4 = list_operations()

    # 問題1-1: スライスでリストの最初の3要素を取得
    assert result1 == [1, 2, 3]

    # 問題1-2: リストを逆順にする
    assert result2 == [5, 4, 3, 2, 1]

    # 問題1-3: リスト内包表記で各要素を2倍にする
    assert result3 == [2, 4, 6, 8, 10]

    # 問題1-4: リストに要素を追加する
    assert result4 == [1, 2, 3, 4, 5, 6, 7, 8]


def test_dict_operations():
    """辞書操作関数のテスト"""
    result1, result2, result3, result4 = dict_operations()

    # 問題2-1: 辞書から安全に値を取得
    assert result1 == "Not found"

    # 問題2-2: 辞書内包表記で各キーと値の長さを持つ辞書を作成
    expected = {"name": 4, "age": 1, "skills": 2}
    assert result2 == expected

    # 問題2-3: 辞書に要素を追加
    expected = {
        "name": "Taro",
        "age": 30,
        "skills": ["Python", "JavaScript"],
        "email": "taro@example.com"
    }
    assert result3 == expected

    # 問題2-4: 辞書のキーと値を入れ替え
    expected = {"Taro": "name"}
    assert result4 == expected


def test_mutability_and_references():
    """可変性と参照に関する関数のテスト"""
    result1, result2, result3 = mutability_and_references()

    # 問題3-1: リストのコピー方法
    original, shallow_copy, deep_copy = result1
    assert original == [1, 2, [99, 4]]
    assert shallow_copy == [1, 2, [99, 4]]  # 浅いコピーなので内部リストの変更が反映される
    assert deep_copy == [1, 2, [3, 4]]  # 深いコピーなので内部リストの変更が反映されない

    # 問題3-2: 可変デフォルト引数の問題
    result2a, result2b, result2c = result2
    assert result2a == [1]
    assert result2b == [2]  # 毎回新しいリストが使われるべき
    assert result2c == [3]  # 毎回新しいリストが使われるべき

    # 問題3-3: 文字列連結とリスト連結の挙動
    str_before_id, str_after_id, list_before_id, list_after_id = result3
    assert str_before_id != str_after_id  # 文字列は新しいオブジェクトが作られる
    assert list_before_id == list_after_id  # リストは同じオブジェクトが使われる


def test_advanced_functions():
    """関数の高度な機能に関する関数のテスト"""
    result1, result2, result3, result4 = advanced_functions()

    # 問題4-1: ラムダ関数を使ったソート
    assert result1 == [1, 2, 3, 4, 5]  # 2乗の小さい順

    # 問題4-2: デコレータ関数
    execution_time, result = result2
    assert isinstance(execution_time, float)
    assert execution_time >= 0.1  # 少なくとも0.1秒はかかるはず
    assert result == "Done!"

    # 問題4-3: 可変長引数と辞書型可変長引数
    required, args, kwargs = result3
    assert required == "必須"
    assert args == (1, 2, 3)
    assert kwargs == {"name": "Taro", "age": 30}

    # 問題4-4: クロージャを使った関数ファクトリ
    double_result, triple_result = result4
    assert double_result == 10  # 5 * 2
    assert triple_result == 15  # 5 * 3


if __name__ == "__main__":
    # pytest.mainを使ってテストを実行
    pytest.main(["-v", __file__])