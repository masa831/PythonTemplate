from concurrent.futures import ProcessPoolExecutor, as_completed
import multiprocessing
import time


def task(x: int) -> int:
    """test"""
    time.sleep(1)
    return x * x


# NOTE: Windows環境でマルチプロセスを動かす場合は、__main__内で使用した方が安全
if __name__ == "__main__":
    start = time.time()
    # map 対象関数の引数にリストを渡したいときに使用する
    print('ProcessPoolExecutor: map core=2')
    inputs = [1, 2, 3, 4, 5]
    with ProcessPoolExecutor(max_workers=2) as executor:  # ワーカー数を制限
        results = list(executor.map(task, inputs))
    print(results)
    print(time.time() - start)

    start = time.time()
    # map 対象関数の引数にリストを渡したいときに使用する
    print('ProcessPoolExecutor: map core=4')
    inputs = [1, 2, 3, 4, 5]
    with ProcessPoolExecutor(max_workers=4) as executor:  # ワーカー数を制限
        results = list(executor.map(task, inputs))
    print(results)
    print(time.time() - start)

    # submit　関数を指定する基本的なメソッド
    print('ProcessPoolExecutor: submit')
    res = []
    with ProcessPoolExecutor(max_workers=2) as executor:  # ワーカー数を制限
        futures = [executor.submit(task, 3) for _ in range(5)]
        for future in as_completed(futures):
            # 終わった処理のindexを追加
            res.append(future.result())
    print(res)

    # mulitprocessing
    print('multiprocessing: map')
    inputs = [1, 2, 3, 4, 5]  # 例としての入力データ
    with multiprocessing.Pool() as pool:
        results = pool.map(task, inputs)  # 並列実行し結果を取得
    print(results)  # [1, 4, 9, 16, 25]
