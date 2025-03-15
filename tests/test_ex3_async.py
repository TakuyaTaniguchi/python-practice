"""
演習3のテスト: 非同期操作のテスト
"""

import pytest
import asyncio
import sys
import os
import time

# テスト対象のモジュールを追加
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from exercises.ex3_async_operations import async_wait, run_parallel, async_counter, AsyncTimer


@pytest.mark.asyncio
async def test_async_wait():
    """非同期待機関数が正しく実装されているかテスト"""
    start_time = time.time()
    result = await async_wait(0.1)
    elapsed = time.time() - start_time
    
    # 戻り値が正しいか確認
    assert result == 0.1
    
    # 少なくとも指定時間だけ待機したか確認
    assert elapsed >= 0.1
    
    # 長すぎる待機でないことを確認（余裕を持たせる）
    assert elapsed < 0.2


@pytest.mark.asyncio
async def test_run_parallel():
    """並行実行関数が正しく実装されているかテスト"""
    wait_times = [0.1, 0.2, 0.3]
    
    # 実行時間を計測
    start_time = time.time()
    results = await run_parallel(wait_times)
    elapsed = time.time() - start_time
    
    # 結果が正しい形式（リスト）で返されるか確認
    assert isinstance(results, list)
    assert len(results) == len(wait_times)
    
    # 各結果が(待機時間, 実際の経過時間)のタプルであることを確認
    for i, (wait_time, actual_time) in enumerate(results):
        assert wait_time == wait_times[i]
        assert actual_time >= wait_time
    
    # 並行実行なので、合計時間は最も長い待機時間より少し長い程度
    assert elapsed >= 0.3  # 最長の待機時間
    assert elapsed < 0.5  # 合計（0.6）より十分短い


@pytest.mark.asyncio
async def test_async_counter():
    """非同期ジェネレータが正しく実装されているかテスト"""
    results = []
    start_time = time.time()
    
    # 非同期ジェネレータを実行して結果を収集
    async for value in async_counter(3, 0.1):
        results.append(value)
    
    elapsed = time.time() - start_time
    
    # 正しい値が生成されたか確認
    assert results == [0, 1, 2]
    
    # 適切な時間間隔で生成されたか確認
    assert elapsed >= 0.2  # 少なくとも 2 * 0.1 秒
    assert elapsed < 0.5  # 余裕を持たせる


@pytest.mark.asyncio
async def test_async_timer():
    """非同期コンテキストマネージャが正しく実装されているかテスト"""
    # 非同期コンテキストマネージャを使用
    async with AsyncTimer() as timer:
        await asyncio.sleep(0.1)
    
    # 経過時間が記録されているか確認
    assert timer >= 0.1
    assert timer < 0.2


if __name__ == "__main__":
    # pytestを実行
    pytest.main(["-v", __file__])