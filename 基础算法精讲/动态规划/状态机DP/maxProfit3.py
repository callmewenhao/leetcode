# -*- coding: utf-8 -*-

"""
@File    : maxProfit3.py
@Author  : wenhao
@Time    : 2023/4/8 19:54
@LC      : 123
"""
from typing import List
from functools import cache
from math import inf


class Solution:
    # 套 k 次的板子
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        @cache
        def dfs(i: int, k: int, hold: bool) -> int:
            if k < 0:
                return -inf
            if i < 0:
                return -inf if hold else 0
            if hold:
                return max(dfs(i - 1, k, True), dfs(i - 1, k - 1, False) - prices[i])
            return max(dfs(i - 1, k, False), dfs(i - 1, k - 1, True) + prices[i])
        return dfs(n - 1, 4, False)
