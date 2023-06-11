# -*- coding: utf-8 -*-

"""
@File    : maxProfit.py
@Author  : wenhao
@Time    : 2023/4/8 19:41
@LC      : 121
"""
from typing import List


class Solution:
    # 同向双指针
    # 维护一个当前最小值
    def maxProfit(self, prices: List[int]) -> int:
        mi = 0
        ans = 0
        for i, p in enumerate(prices):
            if prices[mi] > p:
                mi = i
            ans = max(ans, p - prices[mi])
        return ans
