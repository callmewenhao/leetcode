# -*- coding: utf-8 -*-

"""
@File    : T1.py
@Author  : wenhao
@Time    : 2023/6/25 10:26
@LC      : 
"""
from typing import List
from math import inf, gcd
from functools import cache
from itertools import accumulate
from collections import Counter

class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(i+1, n):
                if gcd(nums[i], nums[j]) == 1:
                    ans += 1
        return ans





