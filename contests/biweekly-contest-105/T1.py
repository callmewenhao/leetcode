# -*- coding: utf-8 -*-

"""
@File    : T1.py
@Author  : wenhao
@Time    : 2023/5/27 22:27
@LC      : 
"""

from typing import List
from math import inf
from functools import cache
from itertools import accumulate
from collections import Counter


class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        x = prices[0] + prices[1]
        return money if x > money else money - x
