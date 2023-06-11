# -*- coding: utf-8 -*-

"""
@File    : maxProfit2.py
@Author  : wenhao
@Time    : 2023/4/6 20:00
@LC      : 122
"""

"""
递归分析
prices = [7,1,5,3,6,4]
从第 0 天开始到第 5 天结束时的利润
== 从第 0 天开始到第 4 天结束时的利润 + 第 5 天的利润 (啥也不干 0, 买入 -4, 卖出 +4)

递归边界
dfs(-1, 0) = 0 第 0 天开始的时候 未持有股票的利润 0
dfs(-1, 1) = -inf 第 0 天开始的时候 持有股票的利润 -inf 不合法的状态

递归入口
dfs(n-1, 0) 第 n - 1 天结束的时候 未持有股票的利润

"""
from typing import List
from functools import cache
from math import inf


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        @cache
        def dfs(i: int, hold: bool) -> int:  # 第 i 天结束之后 hold 状态下的利润
            if i < 0:
                return -inf if hold else 0
            if hold:  # i 天持有股票 = i - 1 天持有股票不作为 or i - 1 天不持有股票+买入
                return max(dfs(i - 1, True), dfs(i - 1, False) - prices[i])
            # i 天不持有股票 = i - 1 天不持有股票不作为 or i - 1 天持有股票+卖出
            return max(dfs(i - 1, False), dfs(i - 1, True) + prices[i])

        return dfs(n - 1, False)  # 答案

    # 翻译成递推
    def maxProfit1(self, prices: List[int]) -> int:
        n = len(prices)
        # 状态 i 的个数应该是 n + 1 因为我们要表示 0 天之前的状态
        f = [[0] * 2 for _ in range(n + 1)]
        f[0][1] = -inf  # 对应 第 0 天开始的时候 持有股票的利润 -inf 不合法的状态

        for i in range(n):
            # i 天不持有股票 = i - 1 天不持有股票不作为 or i - 1 天持有股票+卖出
            f[i + 1][0] = max(f[i][0], f[i][1] + prices[i])
            # i 天持有股票 = i - 1 天持有股票不作为 or i - 1 天不持有股票+买入
            f[i + 1][1] = max(f[i][1], f[i][0] - prices[i])
        return f[n][0]  # 最后一天不持有股票

    # 滚动数组优化
    def maxProfit2(self, prices: List[int]) -> int:
        f0, f1 = 0, -inf
        for num in prices:
            new_f0 = max(f0, f1 + num)
            f1 = max(f1, f0 - num)
            f0 = new_f0

        return f0
