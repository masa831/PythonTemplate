import pandas as pd
from dataclasses import dataclass, field
from itertools import permutations
from typing import List, Dict, Any
import math
import copy
import numpy as np


@dataclass
class Depot:
    id: int
    name: str


@dataclass
class Datasets:
    depots: List[Depot]
    # 動的に設定
    n_depots: int = field(init=False)

    def __post_init__(self):
        n = len(self.depots)
        self.n_depots = len(self.depots)
        # 乱数は固定
        # rng = np.random.default_rng(seed=42)
        rng = np.random.default_rng()
        # n個の都市の (x, y) 座標を 0~100 の範囲で生成
        self.coords = rng.uniform(0, 100, size=(n, 2))
        # マトリクスを生成
        # coords: (n, 2) の配列 [x, y]
        # 1. 差分を計算 (n, 1, 2) - (1, n, 2) = (n, n, 2)
        # これにより、すべてのi, jの組み合わせの(dx, dy)が一気に求まります
        diff = self.coords[:, np.newaxis, :] - self.coords[np.newaxis, :, :]
        # 2. ユークリッド距離を計算 sqrt(dx^2 + dy^2)
        dist_matrix = np.sqrt(np.sum(diff ** 2, axis=-1))
        self.dist_matrix = dist_matrix
        # other: scipyでも可能　簡単かつ早い
        from scipy.spatial.distance import cdist
        dist_matrix_s = cdist(self.coords, self.coords, metric='euclidean')
        self.dist_matrix_s = dist_matrix_s

    @classmethod
    def generate(cls, path: str) -> "Datasets":
        depot_df = pd.read_csv(f"{path}/depot.csv")
        depots = [Depot(id=ind, name=row["name"]) for ind, row in depot_df.iterrows()]

        return cls(depots)
