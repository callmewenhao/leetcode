# -*- coding: utf-8 -*-

"""
@File    : T2.py
@Author  : wenhao
@Time    : 2023/6/18 10:53
@LC      : 
"""
from typing import List
from math import inf
from itertools import pairwise


class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        nums.sort()
        ans = inf
        for x, y in pairwise(nums):
            ans = min(ans, abs(x - y))
        return ans
