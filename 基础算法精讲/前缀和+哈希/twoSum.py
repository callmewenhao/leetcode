# -*- coding: utf-8 -*-

"""
@File    : twoSum.py
@Author  : wenhao
@Time    : 2023/3/12 19:41
@LC      : 1
"""
from typing import List
from collections import Counter


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        c = Counter()
        for i, num in enumerate(nums):
            if (x := target - num) in c:
                return [c[x], i]
            c[num] = i
        return [-1, -1]
