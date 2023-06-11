# -*- coding: utf-8 -*-

"""
@File    : mergeStones.py
@Author  : wenhao
@Time    : 2023/4/4 9:17
@LC      : 1000
"""
from typing import List
from functools import cache
from itertools import accumulate


class Solution:
    # 翻译成递推
    def mergeStones(self, stones: List[int], k: int) -> int:
        n = len(stones)
        if (n - 1) % (k - 1):  # 可行性分析
            return -1
        s = list(accumulate(stones, initial=0))  # 前缀和
        # 注意 dp 的顺序
        f = [[0] * n for _ in range(n)]
        for i in range(n - 1, - 1, -1):
            for j in range(i + 1, n):
                f[i][j] = min(f[i][m] + f[m + 1][j] for m in range(i, j, k - 1))
                if (j - i) % (k - 1) == 0:
                    f[i][j] += s[j + 1] - s[i]
        return f[0][-1]

    # 记搜 灵神真强呀
    def mergeStones2(self, stones: List[int], k: int) -> int:
        n = len(stones)
        if (n - 1) % (k - 1):  # 可行性分析
            return -1
        s = list(accumulate(stones, initial=0))  # 前缀和

        @cache
        def dfs(i: int, j: int) -> int:
            if i == j:
                return 0
            res = min(dfs(i, m) + dfs(m + 1, j) for m in range(i, j, k - 1))
            if (j - i) % (k - 1) == 0:
                res += s[j + 1] - s[i]
            return res

        return dfs(0, n - 1)

    def mergeStones1(self, stones: List[int], k: int) -> int:
        n = len(stones)
        if (n - 1) % (k - 1):  # 可行性分析
            return -1
        s = list(accumulate(stones, initial=0))  # 前缀和

        @cache
        def dfs(i: int, j: int, p: int) -> int:
            if p == 1:  # 合并成一堆
                return 0 if i == j else dfs(i, j, k) + s[j + 1] - s[i]  # 两种情况
            return min(dfs(i, m, 1) + dfs(m + 1, j, p - 1) for m in range(i, j, k - 1))  # k-1 步长 枚举第一组情况

        return dfs(0, n - 1, 1)
