# -*- coding: utf-8 -*-

"""
@File    : countVowelStrings.py
@Author  : wenhao
@Time    : 2023/3/29 9:19
@LC      : 1641
"""
from functools import cache

class Solution:
    # 数学 隔板法 😜
    # 相当于 n+4 个球 选4个位置放隔板
    def countVowelStrings(self, n: int) -> int:
        return (n + 4) * (n + 3) * (n + 2) * (n + 1) // 24

    # 一般的动态规划 👍
    # dp[i][j] 长度为 i 以 j 结尾的字符串数量
    # 递推公式
    # dp[i][j] = sum(dp[i-1][k]) k<=j
    # 边界条件
    # dp[1][k] = 1  k:0-4  也就是长度为 1 的情况
    def countVowelStrings2(self, n: int) -> int:
        dp = [1] * 5
        for _ in range(n - 1):
            for j in range(1, 5):
                dp[j] += dp[j - 1]
        return sum(dp)

    # 第一印象是 数位dp 😁
    def countVowelStrings1(self, n: int) -> int:
        @cache
        def dfs(i: int, last: int) -> int:
            if i > n:
                return 1
            res = 0
            low = last
            up = 5
            for d in range(low, up + 1):
                res += dfs(i + 1, d)
            return res
        return dfs(1, 1)


