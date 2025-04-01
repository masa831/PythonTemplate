# <https://qiita.com/Yukimura127/items/2380931ac5efcd635d05>

import time
import concurrent
from concurrent.futures.process import ProcessPoolExecutor
import random


def task(x: int) -> int:
    t = random.randint(1, 20)
    time.sleep(t)
    print(f'fuction_print: {x=}, {t=}')
    return x


def main():
    st = time.time()
    with ProcessPoolExecutor(max_workers=2) as executor:
        # Future作成
        # 入力データをListで生成する
        data = [i for i in range(5)]
        # 最大実行数分のfutureのリストを生成する
        batch_size = 15
        futures = [executor.submit(task, data) for _ in range(batch_size)]
        # 戻り格納用変数
        results = []
        # 実行
        try:
            timeout = 100
            for future in concurrent.futures.as_completed(futures, timeout):
                result = future.result()
                results.append(result)
                print(f'time={time.time() - st:.3f}: {result=}')
                # 指定数以上の解を得られたら、終了する
                if len(results) >= 6:
                    _force_kill(executor, futures)
                    break

        except concurrent.futures.TimeoutError as _:
            # 現在のfutureの状態を表示
            print(f'Timeout: {_}')
            for future in futures:
                print(id(future), f"running: {future.running()}", f"cancelled: {future.cancelled()}")
            # task kill
            _force_kill(executor, futures)

    # 実行後のfutureの状態を確認
    print("Executor Shutdown -----")
    for future in futures:
        print(id(future), f"running: {future.running()}", f"cancelled: {future.cancelled()} {future._state}")
    print(f'time = {time.time() - st:.3f}')
    print(f'{results=}')


def _force_kill(executor, futures):
    """指定のプロセスを強制終了させる"""
    try:
        for future in futures:
            if not future.running():
                future.cancel()

        # プロセスをKill
        # !! ここを追加 !!
        for process in executor._processes.values():
            # NOTE: おそらくfuture.running() = True, future.cancelled() = Falseのプロセスのみを対象とできればエラーは出ないはず
            print(f'{process.is_alive()} {process.pid}')
            process.kill()

    except Exception as e:
        # NOTE: kill時にエラーが出るようだが、うまくキャッチできない、、、
        print(f'[DBG] error: {e}')


if __name__ == "__main__":
    main()
