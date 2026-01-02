from pyscipopt import Model
import numpy as np
import pandas as pd
from itertools import product, permutations
import copy
from src.dataset import Datasets
from src.parameter import Parameter


class ScipModel:
    def __init__(self, param: Parameter, ds: Datasets):
        self.param = param
        self.ds = ds

    def _formulate(self):
        # 1. モデルの作成
        self.model = Model("TSP")
        self.vars = self._set_decision_variables()
        self._formulate_constraints(self.vars)
        self._formulate_objective(self.vars)

    def _set_decision_variables(self):
        n = self.ds.n_depots

        # 都市 i から都市 j に移動する場合1となるバイナリ変数
        x = np.zeros((n, n), dtype=object)
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                x[i, j] = self.model.addVar(name=f'x[{i}][{j}]', vtype='B')

        # 順序を制御する補助変数 0番目の変数は不要だが、悪いさしないため、そのままにしておく
        u = np.zeros((n), dtype=object)
        for i in range(1, n):
            u[i] = self.model.addVar(name=f'u[{i}]', lb=1, ub=n-1, vtype='C')

        return x, u

    def _formulate_constraints(self, vars):
        x, u = vars
        n = self.ds.n_depots

        # 都市から1回出る
        for i in range(n):
            self.model.addCons(x[i, :].sum() == 1)

        # 都市から1回入る
        for j in range(n):
            self.model.addCons(x[:, j].sum() == 1)

        # MTZ制約(部分巡回除去)
        for i in range(1, n):
            for j in range(1, n):
                if i == j:
                    continue
                self.model.addCons(u[i] - u[j] + n * x[i, j] <= n - 1)

    def _formulate_objective(self, vars):
        p = self.param
        n = self.ds.n_depots

        x, u = vars
        # 距離最短
        obj1 = 0
        for i in range(n):
            for j in range(n):
                obj1 += self.ds.dist_matrix[i, j] * x[i, j]
        # xxx
        obj2 = 0

        self.model.setObjective(p.w_obj1 * obj1 + p.w_obj2 * obj2, "minimize")

    def optimize(self):
        # 定式化
        self._formulate()
        # 最適化時のパラメータ設定
        self.model.setParam("limits/time", self.param.timelimit)
        self.model.setParam("limits/gap", self.param.gap)
        # 最適化の実行
        self.model.optimize()
        print(f'{self.model.getStatus()}')
        print(f'Objective Value: {self.model.getObjVal():.4f}')

        # 結果の取得
        n = self.ds.n_depots
        x, u = self.vars
        x_ans = np.zeros((n, n), dtype=int)
        for i in range(n):
            for j in range(n):
                _x = x[i, j]
                if isinstance(_x, int):
                    continue
                val = self.model.getVal(_x)
                x_ans[i, j] = int(round(val))

        u_ans = np.zeros((n), dtype=int)
        for i in range(n):
            # 暫定対応
            if i == 0:
                continue
            val = self.model.getVal(u[i])
            u_ans[i] = int(round(val))

        ans_vars = {'x': x_ans, 'u': u_ans}

        df_rows = []
        ids = np.nonzero(x_ans)
        inds = np.transpose(ids).tolist()
        for (i_id, j_id,) in inds:
            d1 = self.ds.depots[i_id]
            d2 = self.ds.depots[j_id]
            dist = self.ds.dist_matrix[i_id, j_id]

            df_rows.append({
                "start_dep_id": d1.id,
                "start_dep_name": d1.name,
                "end_dep_id": d2.id,
                "end_dep_name": d2.name,
                "distance": dist
            })
        df = pd.DataFrame(df_rows)

        return df, ans_vars
