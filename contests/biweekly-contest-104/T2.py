# -*- coding: utf-8 -*-

"""
@File    : T2.py
@Author  : wenhao
@Time    : 2023/5/13 22:17
@LC      : 
"""
from typing import List
from math import inf
from functools import cache
from itertools import accumulate
from collections import Counter

class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        for num in nums:
            num.sort(reverse=True)
        ans = 0
        for col in zip(*nums):
            ans += max(col)
        return ans




