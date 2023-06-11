# -*- coding: utf-8 -*-

"""
@File    : maxProfit4.py
@Author  : wenhao
@Time    : 2023/4/8 16:45
@LC      : 188
"""
from typing import List
from functools import cache
from math import inf





class Solution:
    # 买入股票有 k 次限制 次数限制
    # 由于 买入和卖出属于一次交易 我们只需要在其中一个操作中讲 交易次数减 1 就行
    # 或者 这样看 k 次交易意味着 2*k 次操作 这样就可以在每次操作中减 1 了
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)

        @cache
        def dfs(i: int, j: int, hold: bool) -> int:  # 第 i 天结束之后 hold 状态下的利润
            if j < 0:
                return -inf  # 不合法状态
            if i < 0:
                return -inf if hold else 0
            if hold:  # i 天持有股票 = i - 1 天持有股票不作为 or i - 1 天不持有股票+买入
                return max(dfs(i - 1, j, True), dfs(i - 1, j, False) - prices[i])
            # i 天不持有股票 = i - 1 天不持有股票不作为 or i - 1 天持有股票+卖出
            return max(dfs(i - 1, j, False), dfs(i - 1, j - 1, True) + prices[i])

        return dfs(n - 1, k, False)  # 答案

        # 2 * k 版本
        # n = len(prices)
        #
        # @cache
        # def dfs(i: int, j: int, hold: bool) -> int:  # 第 i 天结束之后 hold 状态下的利润
        #     if j < 0:
        #         return -inf  # 不合法状态
        #     if i < 0:
        #         return -inf if hold else 0
        #     if hold:  # i 天持有股票 = i - 1 天持有股票不作为 or i - 1 天不持有股票+买入
        #         return max(dfs(i - 1, j, True), dfs(i - 1, j - 1, False) - prices[i])
        #     # i 天不持有股票 = i - 1 天不持有股票不作为 or i - 1 天持有股票+卖出
        #     return max(dfs(i - 1, j, False), dfs(i - 1, j - 1, True) + prices[i])
        #
        # return dfs(n - 1, 2 * k, False)  # 答案

    # 翻译成递推
    def maxProfit1(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        # k 应该有 0->k 一共 k+1 个状态在考虑边界（非法的状态-1）一共就 k+2 的状态
        f = [[[-inf] * 2 for _ in range(k + 2)] for _ in range(n + 1)]
        for j in range(1, k + 2):
            f[0][j][0] = 0
        for i, p in enumerate(prices):
            for j in range(1, k + 2):
                f[i + 1][j][1] = max(f[i][j][1], f[i][j][0] - p)
                f[i + 1][j][0] = max(f[i][j][0], f[i][j - 1][1] + p)

        return f[n][k + 1][0]

    # 空间优化
    # 倒序处理覆盖问题
    def maxProfit2(self, k: int, prices: List[int]) -> int:
        # k 应该有 0->k 一共 k+1 个状态在考虑边界（非法的状态-1）一共就 k+2 的状态
        f = [[-inf] * 2 for _ in range(k + 2)]
        for j in range(1, k + 2):
            f[j][0] = 0
        for i, p in enumerate(prices):
            for j in range(k + 1, 0, -1):
                f[j][1] = max(f[j][1], f[j][0] - p)  # 由于 f[j][1] 要用到 f[j][0] 所以先算 f[j][1]
                f[j][0] = max(f[j][0], f[j - 1][1] + p)

        return f[k + 1][0]
