# -*- coding: utf-8 -*-

"""
@File    : getMaximumConsecutive.py
@Author  : wenhao
@Time    : 2023/2/4 12:41
@LC      : 1798
"""
from typing import List

class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        end = 0
        coins.sort()

        for i, coin in enumerate(coins):
            if coin > end + 1:
                break
            end = end + coin
        return end + 1

