"""
poolを利用したときに、複数の引数を対象関数に渡す方法
wrapper関数を用意する。

"""

from multiprocessing import Pool
from time import sleep
import time


def do(waitTime, display):
    print(f'start {waitTime=}, {display=}')
    sleep(waitTime)
    return waitTime


def wrapper(args):
	return do(*args)


if __name__ == '__main__':
    waitTimes = [3, 20, 1, 6, 4]
    d_num = [1, 2, 3, 4, 5]
    args = [(i, j) for i, j in zip(waitTimes, d_num)]
    timeout_sec = 5
    start = time.time()

    # パターン１
    with Pool(10) as p:
        results = p.map(wrapper, args)  # imap_unorderedをmapに変更
        for result in results:
            print("result waitTime:{} 開始から{}秒経過".format(result, time.time() - start))
