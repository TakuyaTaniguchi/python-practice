"""
演習4: Python基本文法演習

この演習では、Pythonの基本的な文法と機能を学習します。
TypeScriptやRubyからPythonに移行する際に特に注意すべきポイントに焦点を当てています。
"""


# 問題1: リスト操作
# Pythonのリスト操作を理解しましょう
# TODO: 以下の関数を実装してください

def list_operations():
    """
    Pythonのリスト操作に関する関数

    戻り値: 各操作結果のタプル (result1, result2, result3, result4)
    """
    # 元のリスト
    original = [1, 2, 3, 4, 5]

    # 問題1-1: スライスを使って、リストの最初の3要素を取得してください
    # ヒント: [start:end] 形式を使用します
    result1 = original[0:3] # ここを実装

    # 問題1-2: 元のリストを変更せずに、リストの要素を逆順にした新しいリストを作成してください
    # ヒント: スライスのステップパラメータを使用します
    result2 = original[::-1]  # ここを実装

    # 問題1-3: リスト内包表記を使って、originalリストの各要素を2倍にした新しいリストを作成してください
    # ヒント: [expression for item in iterable]
    result3 = [i*2 for i in original] # ここを実装

    # 問題1-4: 元のリストを破壊的に変更して、リストに[6, 7, 8]を追加してください
    # ヒント: extendメソッドを使用します

    # Note extendメソッドは戻り値がNoneである。
    original.extend((6, 7, 8))
    result4 = original  # ここを実装し、originalリストを返す

    return result1, result2, result3, result4


# 問題2: 辞書（ディクショナリ）操作
# Pythonの辞書操作を理解しましょう
# TODO: 以下の関数を実装してください

def dict_operations():
    """
    Pythonの辞書操作に関する関数

    戻り値: 各操作結果のタプル (result1, result2, result3, result4)
    """
    # 元の辞書
    user = {
        "name": "Taro",
        "age": 30,
        "skills": ["Python", "JavaScript"]
    }

    # 問題2-1: 辞書から安全に'email'キーの値を取得してください（キーが存在しない場合は'Not found'を返す）
    # ヒント: getメソッドを使用します
    result1 = None  # ここを実装

    # 問題2-2: 辞書内包表記を使って、userの各キーとその値の長さ（文字列の場合は長さ、リストの場合は要素数）を持つ新しい辞書を作成してください
    # ヒント: {key: expression for (key, value) in dictionary.items()}
    result2 = None  # ここを実装

    # 問題2-3: 元の辞書に'email'キーと値'taro@example.com'を追加し、更新された辞書を返してください
    # ヒント: 辞書の更新方法を使用します
    result3 = None  # ここを実装

    # 問題2-4: 辞書のキーと値を入れ替えた新しい辞書を作成してください（値が文字列の場合のみ）
    # ヒント: 条件付き辞書内包表記を使用します
    result4 = None  # ここを実装

    return (result1, result2, result3, result4)


# 問題3: 可変オブジェクトと参照
# Pythonの可変性と参照の概念を理解しましょう
# TODO: 以下の関数を実装してください

def mutability_and_references():
    """
    Pythonの可変性と参照に関する関数

    戻り値: 各操作結果のタプル (result1, result2, result3)
    """
    # 問題3-1: リストのコピー方法の違いを確認してください
    original = [1, 2, [3, 4]]

    # 浅いコピー
    shallow_copy = original.copy()

    # 深いコピー
    import copy
    deep_copy = copy.deepcopy(original)

    # original内のネストしたリストを変更
    original[2][0] = 99

    # shallow_copyとdeep_copyの内容を確認
    # 浅いコピーの場合、内部リストは参照されたままなので変更が反映される
    # 深いコピーの場合、内部リストも含めて完全にコピーされるので元のリストの変更は反映されない
    result1 = (original, shallow_copy, deep_copy)

    # 問題3-2: 関数引数における可変デフォルト引数の問題を実演してください
    def append_to_list(item, target_list=None):
        """
        アイテムをリストに追加する関数
        可変オブジェクトをデフォルト引数として使用する際の注意点を示す

        ヒント: Noneをデフォルト値とし、関数内で初期化するパターンを使用します
        """
        # ここを実装
        pass

    # 関数を複数回呼び出し
    result2a = append_to_list(1)
    result2b = append_to_list(2)
    result2c = append_to_list(3)

    result2 = (result2a, result2b, result2c)

    # 問題3-3: 文字列（イミュータブル）と+=演算子の挙動を確認してください
    def string_concatenation():
        """
        文字列連結における+=演算子の挙動を確認する関数
        """
        # ここを実装：
        # 1. 文字列に+=演算子を使用して連結
        # 2. リストに+=演算子を使用して連結
        # 3. idを使って元のオブジェクトと同じかどうかを確認
        pass

    result3 = string_concatenation()

    return (result1, result2, result3)


# 問題4: 関数の高度な機能
# Pythonの関数の高度な機能を理解しましょう
# TODO: 以下の関数を実装してください

def advanced_functions():
    """
    Pythonの関数の高度な機能に関する関数

    戻り値: 各操作結果のタプル (result1, result2, result3, result4)
    """
    # 問題4-1: ラムダ関数を使用して、数値のリストを各要素の2乗でソートしてください
    numbers = [1, 5, 2, 4, 3]
    # ヒント: sortedとkeyパラメータを使用します
    result1 = None  # ここを実装

    # 問題4-2: デコレータ関数を実装してください
    # 関数の実行時間を計測するデコレータを作成します
    def timing_decorator(func):
        """
        関数の実行時間を計測するデコレータ
        """
        # ここを実装
        pass

    # デコレータを使用する関数
    @timing_decorator
    def slow_function():
        import time
        time.sleep(0.1)
        return "Done!"

    result2 = slow_function()

    # 問題4-3: 可変長引数と辞書型可変長引数を使用する関数を実装してください
    # ヒント: *args, **kwargsを使用します
    def flexible_function(required_arg, *args, **kwargs):
        """
        必須引数、可変長引数、辞書型可変長引数を受け取る関数
        """
        # ここを実装
        pass

    result3 = flexible_function("必須", 1, 2, 3, name="Taro", age=30)

    # 問題4-4: クロージャを使用して、関数ファクトリを実装してください
    def multiplier_factory(factor):
        """
        指定された係数を使用して乗算を行う関数を返すファクトリ関数
        """
        # ここを実装
        pass

    # 2倍にする関数と3倍にする関数を作成
    double = multiplier_factory(2)
    triple = multiplier_factory(3)

    result4 = (double(5), triple(5))

    return (result1, result2, result3, result4)