import time
from functools import wraps
from loguru import logger
from typing import Dict, Optional


class Timer:
    def __init__(self):
        # 最終的な計測結果 {変数名: 経過時間(秒)}
        self._results: Dict[str, float] = {}
        # setメソッドで開始した時刻を一時保持 {変数名: 開始時刻}
        self._start_times: Dict[str, float] = {}

    def set(self, name: str):
        """
        計測を開始します。
        """
        self._start_times[name] = time.perf_counter()
        logger.info(f"SET  [{name}]: 計測を開始しました")

    def end(self, name: str):
        """
        set関数で開始した計測を終了し、処理時間を算出・保存します。
        """
        if name not in self._start_times:
            logger.error(f"END  [{name}]: set('{name}') が呼ばれていません")
            return

        end_time = time.perf_counter()
        elapsed = end_time - self._start_times.pop(name)
        self._results[name] = elapsed
        logger.info(f"END  [{name}]: {elapsed:.4f}s")

    def start(self, name: str):
        """
        デコレータとして使用し、関数全体の処理時間を計測します。
        """
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                self.set(name)
                result = func(*args, **kwargs)
                self.end(name)
                return result
            return wrapper
        return decorator

    def get_results(self) -> Dict[str, float]:
        """保持している全計測結果を返します。"""
        return self._results

    def clear(self):
        """全ての計測データと一時データをリセットします。"""
        self._results = {}
        self._start_times = {}


# インスタンス化してエクスポート
timer = Timer()
