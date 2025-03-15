"""
演習3: 非同期操作の実装

この演習では、Python/FastAPIの非同期処理を学びます。
TypeScriptのasync/awaitに似た概念ですが、内部実装が異なります。
"""

import asyncio
from typing import List, Dict, Any
import time

# 問題1: 非同期関数を作成してください
# 指定された秒数だけ非同期に待機し、その秒数を返す関数
# ヒント: asyncioモジュールのsleep関数を使用します
# TODO: ここにasync_wait関数を実装


# 問題2: 複数の非同期処理を並行実行する関数を作成してください
# wait_times: 待機時間のリスト
# 戻り値: 各待機時間と実際にかかった時間のペアのリスト
# ヒント: asyncio.gatherを使用してください
# TODO: ここにrun_parallel関数を実装


# 問題3: 非同期ジェネレータ関数を作成してください
# count: 生成する数値の数
# interval: 各数値間の待機時間（秒）
# 0からcount-1までの数値を順番に生成し、interval秒ごとに待機します
# ヒント: asyncキーワードとyieldキーワードを組み合わせて使用します
# TODO: ここにasync_counter関数を実装


# 問題4: 非同期コンテキストマネージャを作成してください
# タイマー機能を持つコンテキストマネージャを作成します
# enter時に時間を記録し、exit時に経過時間を表示・返却する
# ヒント: __aenter__と__aexit__メソッドを実装します
# TODO: ここにAsyncTimerクラスを実装