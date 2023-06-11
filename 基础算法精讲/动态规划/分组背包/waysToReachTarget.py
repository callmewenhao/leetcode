# -*- coding: utf-8 -*-

"""
@File    : waysToReachTarget.py
@Author  : wenhao
@Time    : 2023/3/31 21:13
@LC      : 2585
"""
from typing import List


class Solution:

    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        new_mark = []

        for count, mark in types:
            c = 1
            while count > c:
                count -= c
                new_mark.append(c * mark)
                c *= 2
            new_mark.append(count * mark)

        dp = [0] * (target + 1)
        dp[0] = 1
        for i, mark in enumerate(new_mark):
            for j in range(target, mark - 1, -1):
                dp[j] += dp[j - mark]
                dp[j] %= MOD
        return dp[-1]


    def waysToReachTarget1(self, target: int, types: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        dp = [0] * (target + 1)
        dp[0] = 1

        for i, count, mark in enumerate(types):
            for j in range(target, mark - 1, -1):
                for k in range(1, min(count, j // mark) + 1):  # 一维的递推 下标从 1 开始就行
                    dp[j] += dp[j - k * mark]
                    dp[j] %= MOD
        return dp[-1]

        




