# -*- coding: utf-8 -*-

"""
@File    : longestPalindromeSubseq.py
@Author  : wenhao
@Time    : 2023/4/4 10:47
@LC      : 516
"""
from functools import cache


class Solution:
    # 空间优化
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        f = [0] * n  # 很多 i > j 的情况都是 0

        for i in range(n - 1, -1, -1):
            f[i] = 1  # 同一个位置
            last = 0  # 保存被覆盖的值
            for j in range(i + 1, n):
                temp = f[j]
                if s[i] == s[j]:  # 两端相等
                    f[j] = last + 2
                else:  # 两端不等 取最大
                    f[j] = max(f[j], f[j - 1])
                last = temp
        return f[n - 1]

    # 递推
    def longestPalindromeSubseq2(self, s: str) -> int:
        n = len(s)
        f = [[0] * n for _ in range(n)]  # 很多 i > j 的情况都是 0

        for i in range(n - 1, -1, -1):
            f[i][i] = 1  # 同一个位置
            for j in range(i + 1, n):
                if s[i] == s[j]:  # 两端相等
                    f[i][j] = f[i + 1][j - 1] + 2
                else:  # 两端不等 取最大
                    f[i][j] = max(f[i + 1][j], f[i][j - 1])
        return f[0][n - 1]

    # 记搜 😜
    def longestPalindromeSubseq1(self, s: str) -> int:
        n = len(s)

        @cache
        def dfs(i: int, j: int) -> int:
            if i > j: return 0  # 区间不存在
            if i == j: return 1  # 单独一个数
            if s[i] == s[j]:
                return dfs(i + 1, j - 1) + 2  # 两端相等
            return max(dfs(i, j - 1) + 1, dfs(i + 1, j) + 1)  # 两端不等取最大

        return dfs(0, n - 1)
