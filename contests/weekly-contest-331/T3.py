# -*- coding: utf-8 -*-

"""
@File    : T3.py
@Author  : wenhao
@Time    : 2023/2/5 10:01
@LC      : 
"""
from typing import List
from bisect import bisect_left


class Solution:

    # optimize 滚动数组
    def minCapability(self, nums: List[int], k: int) -> int:
        n = len(nums)

        def check(mx: int) -> int:
            f0, f1 = 0, 0
            for i, num in enumerate(nums):
                if num <= mx:
                    f0, f1 = f1, max(f0 + 1, f1)
                else:
                    f0 = f1
            return f1

        return bisect_left(range(max(nums)), k, key=check)

