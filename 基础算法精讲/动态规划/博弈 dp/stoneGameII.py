# -*- coding: utf-8 -*-

"""
@File    : stoneGameII.py
@Author  : wenhao
@Time    : 2023/2/22 8:53
@LC      : 1140
"""
from typing import List
from functools import cache


class Solution:
    # 1比1翻译成递推
    def stoneGameII3(self, piles: List[int]) -> int:
        s, n = 0, len(piles)
        f = [[0] * (n + 1) for _ in range(n)]
        for i in range(n - 1, -1, -1):
            s += piles[i]
            for m in range(1, i // 2 + 2):
                if i + m * 2 >= n:
                    f[i][m] = s
                else:
                    f[i][m] = s - min(f[i + x][max(m, x)] for x in range(1, m * 2 + 1))
        return f[0][1]

    # 改成记忆化搜索
    # 记忆化的边界：
    # 为了在 i 尽量小的情况下，使 M 尽量大，那么每次都拿满 2M 堆
    # 最后有 (2+4+8+⋯+M)+2M < n 等比数列求和=> 4M−2 < n 一共有 n 堆但是取不到 n
    # 4M ≤ n+1 则 M 的上界为 int((n + 1) / 4)
    def stoneGameII2(self, s: List[int]) -> int:
        n = len(s)
        for i in range(n - 2, -1, -1):
            s[i] += s[i + 1]  # 后缀和

        @cache
        def dfs(i: int, m: int):
            if i + m * 2 >= n:
                return s[i]
            return s[i] - min(dfs(i + x, max(m, x)) for x in range(1, m * 2 + 1))

        return dfs(0, 1)

    # 用后缀和表示能够选取的剩余堆石头数目
    # Alice 能够拿到的最大数目 = 剩余堆石头数目 - Bob 能拿到的最小石头数目
    # dfs(i, M) = s[i] - min^{2M}_{X=1} dfs(i+X, max(M, X))
    # Alice 先手，答案就是 dfs(0, 1)
    def stoneGameII1(self, s: List[int]) -> int:
        n = len(s)
        for i in range(n - 2, -1, -1):
            s[i] += s[i + 1]  # 后缀和

        def dfs(i: int, m: int):
            if i + m * 2 >= n:
                return s[i]
            return s[i] - min(dfs(i + x, max(m, x)) for x in range(1, m * 2 + 1))

        return dfs(0, 1)  # 超出时间限制😢
