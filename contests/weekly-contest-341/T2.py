# -*- coding: utf-8 -*-

"""
@File    : T2.py
@Author  : wenhao
@Time    : 2023/4/16 10:07
@LC      : 
"""
from typing import List
from collections import Counter



class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        m = len(nums)
        n = len(divisors)

        s = [0] * n
        for i in range(n):
            s[i] = sum(num % divisors[i] == 0 for num in nums)

        idx = 0
        for i in range(n):
            if s[idx] < s[i]:
                idx = i
            if s[idx] == s[i] and divisors[idx] > divisors[i]:
                idx = i
        return divisors[idx]

