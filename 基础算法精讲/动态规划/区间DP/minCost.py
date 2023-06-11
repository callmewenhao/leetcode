# -*- coding: utf-8 -*-

"""
@File    : minCost.py
@Author  : wenhao
@Time    : 2023/4/5 20:21
@LC      : 1547
"""
from typing import List
from functools import cache
from math import inf


class Solution:
    # 区间 DP 记搜 👍
    def minCost(self, n: int, cuts: List[int]) -> int:
        # 想法是 待切割的木棍和切割点的区间对应起来 所以要进行排序
        l = len(cuts)
        cuts.sort()

        # s, e, i, j 代表 木棍起点 终点 切点数组区间起点 终点
        # s, e 和 i, j 是对应的 时间复杂度并不是 4 + 1 = 5 次方 还是 2 + 1 = 3 次方。
        @cache
        def dfs(s: int, e: int, i: int, j: int) -> int:
            # print(s, e, i, j)
            if i > j:  # 不用切 代价为 0
                return 0
            if i == j:  # 切 1 🔪
                return e - s
            # 切好多🔪🔪🔪🔪🔪
            res = inf
            for k in range(i, j + 1):  # 枚举切的位置 找最小值
                res = min(res, dfs(s, cuts[k], i, k - 1) + dfs(cuts[k], e, k + 1, j))
            return res + e - s

        return dfs(0, n, 0, l - 1)  # 答案

    # 对记搜进行优化
    def minCost1(self, n: int, cuts: List[int]) -> int:
        # 在 cuts 中加上 0 和 n 把木棍和切割区间统一起来
        m = len(cuts)
        cuts = [0] + sorted(cuts) + [n]

        @cache
        def dfs(i: int, j: int) -> int:
            # print(s, e, i, j)
            if i > j:  # 不用切 代价为 0
                return 0
            if i == j:  # 切 1 🔪
                return cuts[j + 1] - cuts[i - 1]
            # 切好多🔪🔪🔪🔪🔪
            # 枚举切哪刀
            res = inf
            for k in range(i, j + 1):  # 枚举切的位置 找最小值
                res = min(res, dfs(i, k - 1) + dfs(k + 1, j))
            return res + cuts[j + 1] - cuts[i - 1]  # 注意 i j 是能切的🔪 而区间端点应该在 i-1 j+1 位置

        return dfs(1, m)  # 答案

    # 改成递推
    def minCost2(self, n: int, cuts: List[int]) -> int:
        m = len(cuts)
        cuts = [0] + sorted(cuts) + [n]
        f = [[0] * (m + 2) for _ in range(m + 2)]

        for i in range(m, 0, -1):
            f[i][i] = cuts[i + 1] - cuts[i - 1]
            for j in range(i + 1, m + 1):
                res = inf
                for k in range(i, j + 1):
                    res = min(res, f[i][k - 1] + f[k + 1][j])
                f[i][j] = res + cuts[j + 1] - cuts[i - 1]

        return f[1][m]

