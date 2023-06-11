# -*- coding: utf-8 -*-

"""
@File    : maxProfitWithCooldown.py
@Author  : wenhao
@Time    : 2023/4/8 16:37
@LC      : 309
"""
from typing import List
from functools import cache
from math import inf


class Solution:
    # 这一题中 卖出之后不允许立即买入 间隔变成 2
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        @cache
        def dfs(i: int, hold: bool) -> int:  # 第 i 天结束之后 hold 状态下的利润
            if i < 0:
                return -inf if hold else 0
            if hold:  # i 天持有股票 = i - 1 天持有股票不作为 or i - 2 天不持有股票+买入
                return max(dfs(i - 1, True), dfs(i - 2, False) - prices[i])
            # i 天不持有股票 = i - 1 天不持有股票不作为 or i - 1 天持有股票+卖出
            return max(dfs(i - 1, False), dfs(i - 1, True) + prices[i])

        return dfs(n - 1, False)  # 答案
