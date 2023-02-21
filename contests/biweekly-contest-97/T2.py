# -*- coding: utf-8 -*-

"""
@File    : T2.py
@Author  : wenhao
@Time    : 2023/2/4 22:16
@LC      : 
"""

from typing import List
from collections import Counter

class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        s = set(banned)
        nums = [num for num in range(1, n + 1) if num not in s]
        nums.sort()

        ans = 0
        sum = 0
        for i, num in enumerate(nums):
            if sum + num > maxSum:
                break
            ans += 1
            sum += num
        return ans
