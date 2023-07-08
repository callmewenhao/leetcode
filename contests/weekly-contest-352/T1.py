# -*- coding: utf-8 -*-

"""
@File    : T1.py
@Author  : wenhao
@Time    : 2023/7/2 10:21
@LC      : 
"""

from typing import List
from math import inf, gcd
from functools import cache
from itertools import accumulate
from collections import Counter


class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        ans = 0
        for i, x in enumerate(nums):
            if x <= threshold and x % 2 == 0:
                ans = max(ans, 1)
                for j, y in enumerate(nums[i + 1:], 1):
                    if y <= threshold and y % 2 == j % 2:
                        ans = max(ans, j + 1)
                        continue
                    if y > threshold or y <= threshold and y % 2 != j % 2:
                        break
        return ans
