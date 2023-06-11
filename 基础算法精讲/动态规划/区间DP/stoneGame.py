# -*- coding: utf-8 -*-

"""
@File    : stoneGame.py
@Author  : wenhao
@Time    : 2023/4/5 11:57
@LC      : 877
"""
from typing import List
from functools import cache


class Solution:
    # 翻译成递推
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        f = [[0] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            f[i][i] = piles[i]
            for j in range(i + 1, n):
                f[i][j] = max(piles[i] - f[i + 1][j], piles[j] - f[i][j - 1])

        return f[0][n - 1] > 0

    # 记搜
    def stoneGame3(self, piles: List[int]) -> bool:
        n = len(piles)

        # dfs(i, j) 表示当前人比另一个人多的值
        @cache
        def dfs(i: int, j: int) -> int:
            if i > j: return 0
            if i == j: return piles[i]

            return max(piles[i] - dfs(i + 1, j), piles[j] - dfs(i, j - 1))

        return dfs(0, n - 1)

    # 贪心 也类似区间 DP 其实是做错了 😭
    def stoneGame2(self, piles: List[int]) -> bool:
        n = len(piles)
        s = sum(piles)

        def dfs(i: int, j: int) -> int:
            if i > j:
                return 0
            return max(piles[i], piles[j]) + dfs(i + 1, j - 1)

        Alices = dfs(0, n - 1)

        return True if Alices > s - Alices else False

    # 猜个答案 😁
    def stoneGame1(self, piles: List[int]) -> bool:
        return True
