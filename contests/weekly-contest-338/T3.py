# -*- coding: utf-8 -*-

"""
@File    : T3.py
@Author  : wenhao
@Time    : 2023/3/26 10:16
@LC      : 
"""
from typing import List
from collections import Counter
from bisect import bisect_left
from itertools import accumulate


class Solution:
    # 经典技巧综合应用 😁
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        s = sum(nums)
        prefix = list(accumulate(nums, initial=0))

        ans = []
        for q in queries:
            idx = bisect_left(nums, q)
            s1 = prefix[idx]
            s2 = s - s1
            ans.append(idx * q - s1 + s2 - (n - idx) * q)
        return ans
