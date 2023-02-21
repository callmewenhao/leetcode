# -*- coding: utf-8 -*-

"""
@File    : dieSimulator.py
@Author  : wenhao
@Time    : 2023/2/10 10:00
@LC      : 1223
"""
from typing import List
from functools import cache


class Solution:
    # 使用dp 递推
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        MOD = 10 ** 9 + 7
        m = len(rollMax)  # 6
        f = [[[0] * mx for mx in rollMax] for _ in range(n)]
        f[0] = [[1] * mx for mx in rollMax]
        for i in range(1, n):
            for last, mx in enumerate(rollMax):
                for left in range(mx):
                    res = 0
                    for j in range(m):
                        if j != last:
                            res += f[i - 1][j][-1]
                        elif left:
                            res += f[i - 1][j][left - 1]
                    f[i][last][left] = res % MOD
        return sum(f[-1][j][-1] for j in range(m)) % MOD

    # 使用记忆化搜索优化时间复杂度
    def dieSimulator2(self, n: int, rollMax: List[int]) -> int:
        MOD = 10 ** 9 + 7

        @cache
        def dfs(i: int, last: int, left: int) -> int:
            if i == 0:
                return 1
            res = 0
            for j, mx in enumerate(rollMax):
                if j != last:
                    res += dfs(i - 1, j, mx - 1)
                elif left:
                    res += dfs(i - 1, j, left - 1)
            return res % MOD

        return sum(dfs(n - 1, j, mx - 1) for j, mx in enumerate(rollMax)) % MOD

    # 回溯写法
    def dieSimulator1(self, n: int, rollMax: List[int]) -> int:
        MOD = 10 ** 9 + 7

        def dfs(i: int, last: int, left: int) -> int:
            if i == 0:
                return 1
            res = 0
            for j, mx in enumerate(rollMax):
                if j != last:
                    res += dfs(i - 1, j, mx - 1)
                elif left:
                    res += dfs(i - 1, j, left - 1)
            return res % MOD

        return sum(dfs(n - 1, j, mx - 1) for j, mx in enumerate(rollMax)) % MOD
