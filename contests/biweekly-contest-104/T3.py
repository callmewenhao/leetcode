# -*- coding: utf-8 -*-

"""
@File    : T3.py
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
    def maximumOr(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_or = [0] * n
        for i in range(n - 1):
            prefix_or[i + 1] = prefix_or[i] | nums[i]
        suffix_or = [0] * n
        for i in range(n - 1, 0, -1):
            suffix_or[i - 1] = suffix_or[i] | nums[i]
        # 贪心 k 次
        ans = 0
        for i, num in enumerate(nums):
            ans = max(ans, (num << k) | prefix_or[i] | suffix_or[i])
        return ans
