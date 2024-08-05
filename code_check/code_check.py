import numpy as np


def _test_ng():
    print('hello,world')


def _test_ok() -> None:
    print('hello,world')


def myadd(x: int, y: int) -> int:
    """xxxx

    Args:
        x (int): _description_
        y (int): _description_

    Returns:
        int: _description_
    """
    return x + y

def tes() -> None:
    print('aaa')


if __name__ == "__main__":
    a = 1
    b = 2
    c = 2.3

    z = myadd(a, b)
    z1 = myadd(a,c)
    print(z)
