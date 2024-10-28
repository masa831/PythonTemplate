from typing import Optional


# Optional　NGケース
def ng_get_id(name: str) -> int:
    """xxx"""
    ret = None
    if name == 'A':
        ret = 1
    return ret


# Optional　OKケース
def get_id(name: str) -> Optional[int]:
    """xxx"""
    ret = None
    if name == 'A':
        ret = 1
    return ret


# Optional　OKケース
def test(x: Optional[int] = None) -> None:
    """xxx"""
    print(x)
