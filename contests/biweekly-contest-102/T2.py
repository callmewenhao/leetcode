# -*- coding: utf-8 -*-

"""
@File    : T2.py
@Author  : wenhao
@Time    : 2023/4/15 22:24
@LC      : 
"""
from typing import List
from itertools import accumulate
from collections import Counter


class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        n = len(nums)

        m = [nums[0]] * n
        for i in range(1, n):
            m[i] = max(m[i - 1], nums[i])
        print(m)

        conver = [0] * n
        for i in range(n):
            conver[i] = nums[i] + m[i]
        print(conver)

        ans = accumulate(conver)
        return ans
