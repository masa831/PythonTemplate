# src/loader.py
import pandas as pd
from src.utils import resolve_path_from_root

def load_csv(filename: str) -> pd.DataFrame:
    """
    プロジェクトルートから data/filename を読み込む。
    """
    path = resolve_path_from_root("data", filename)
    print(f'[DBG] {path=}')
    return pd.read_csv(path)


def bf_load_csv(filename: str):
    # return pd.read_csv('../data/sample.csv')
    return pd.read_csv('./data/sample.csv')
