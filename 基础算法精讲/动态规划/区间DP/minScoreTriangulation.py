# -*- coding: utf-8 -*-

"""
@File    : minScoreTriangulation.py
@Author  : wenhao
@Time    : 2023/4/2 9:56
@LC      : 1039
"""
from typing import List
from functools import cache
from math import inf


class Solution:
    # 递推
    def minScoreTriangulation(self, v: List[int]) -> int:
        n = len(v)
        f = [[0] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):  # 对应记搜参数 i
            for j in range(i + 1, n):  # 对应记搜参数 j
                if i + 1 == j:  # 只有两点时返回 0 无法组成三角形  其实这个 if 可以省略
                    f[i][j] = 0
                else:
                    # 找一个最小值
                    f[i][j] = min(f[i][m] + f[m][j] + v[i] * v[m] * v[j] for m in range(i + 1, j))

        return f[0][n - 1]  # 答案

    # 记搜
    def minScoreTriangulation1(self, v: List[int]) -> int:
        n = len(v)

        @cache
        def dfs(i: int, j: int) -> int:
            if i + 1 >= j:  # 其实等于也 OK
                return 0
            res = inf
            for k in range(i + 1, j):
                res = min(res, dfs(i, k) + dfs(k, j) + v[i] * v[k] * v[j])
            return res

        return dfs(0, n - 1)
