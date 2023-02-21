# -*- coding: utf-8 -*-

"""
@File    : T2.py
@Author  : wenhao
@Time    : 2023/2/18 22:20
@LC      : 6361
"""

from typing import List
from collections import Counter
from collections import deque

class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 3:
            return 0

        nums.sort()
        a = nums[-1] - nums[2]
        b = nums[-3] - nums[0]
        c = nums[-2] - nums[1]

        return min(a, b, c)









