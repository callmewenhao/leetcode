# -*- coding: utf-8 -*-

"""
@File    : maxProfitWithFee.py
@Author  : wenhao
@Time    : 2023/4/8 20:09
@LC      : 714
"""
from typing import List
from functools import cache
from math import inf

class Solution:
    # 每次交易完成之后（我选卖出之后）要缴费 fee 元
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)

        @cache
        def dfs(i: int, hold: bool) -> int:
            if i < 0:
                return -inf if hold else 0
            if hold:
                return max(dfs(i - 1, True), dfs(i - 1, False) - prices[i])
            return max(dfs(i - 1, False), dfs(i - 1, True) + prices[i] - 2)

        return dfs(n - 1, False)













