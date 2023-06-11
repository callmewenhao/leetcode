# -*- coding: utf-8 -*-

"""
@File    : T3.py
@Author  : wenhao
@Time    : 2023/5/27 22:27
@LC      : 
"""

from typing import List
from math import inf
from functools import cache
from itertools import accumulate
from collections import Counter


class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        pos = []
        neg = []
        for num in nums:
            if num > 0:
                pos.append(num)
            if num < 0:
                neg.append(num)
        pos.sort()
        neg.sort()

        ans = 1
        for num in pos:
            ans *= num

        n = len(neg)
        for i in range(n // 2):
            ans *= neg[i * 2] * neg[i * 2 + 1]
        return ans

