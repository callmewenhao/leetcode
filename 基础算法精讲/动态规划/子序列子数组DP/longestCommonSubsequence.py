# -*- coding: utf-8 -*-

"""
@File    : longestCommonSubsequence.py
@Author  : wenhao
@Time    : 2023/2/28 16:05
@LC      : 1143
"""
from typing import List
from functools import cache


class Solution:
    # 递推优化 一维数组
    def longestCommonSubsequence3(self, s: str, t: str) -> int:
        n = len(s)
        f = [0] * (n + 1)

        for i, x in enumerate(t):  # t 对应行
            prev = f[0]  # prev=0 😊 记录 f[i][j]
            for j, y in enumerate(s):  # s 对应列
                t = f[j + 1]  # 存新的 f[i][j]
                f[j + 1] = prev + 1 if x == y else max(f[j + 1], f[j])
                prev = t  # 更新 f[i][j]
        return f[-1]

    # 递推 二维数组
    def longestCommonSubsequence2(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)

        f = [[0] * (n + 1) for _ in range(m + 1)]
        for i, x in enumerate(t):  # t 对应行
            for j, y in enumerate(s):  # s 对应列
                f[i + 1][j + 1] = f[i][j] + 1 if x == y else max(f[i][j + 1], f[i + 1][j])
        return f[m][n]

    # 记忆化搜索
    def longestCommonSubsequence1(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)

        @cache
        def dfs(i: int, j: int) -> int:
            if i < 0 or j < 0:  # 当某一串为空串时 LCS 必然为 0
                return 0
            if s[i] == t[j]:  # i j 对应的字符相等时 只需看前 i-1 和 j-1 对应的字串 LCS 即可
                return dfs(i - 1, j - 1) + 1
            # 不相等时 答案必然为 下面两个情况中的最大值
            return max(dfs(i, j - 1), dfs(i - 1, j))

        return dfs(n - 1, m - 1)  # 返回答案
