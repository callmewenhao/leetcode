# -*- coding: utf-8 -*-

"""
@File    : T2.py
@Author  : wenhao
@Time    : 2023/6/4 10:20
@LC      : 
"""
from typing import List
from math import inf
from functools import cache
from itertools import accumulate
from collections import Counter

class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:

        n = len(nums)
        if nums[0] == 1 and nums[-1] == n:
            return 0

        ans = 0
        idx_1 = nums.index(1)
        idx_n = nums.index(n)
        ans  = idx_1 + n - 1 - idx_n
        if idx_1 > idx_n:
            ans -= 1
        return ans
