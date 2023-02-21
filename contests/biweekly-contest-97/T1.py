# -*- coding: utf-8 -*-

"""
@File    : T1.py
@Author  : wenhao
@Time    : 2023/2/4 22:16
@LC      : 
"""

from typing import List
from collections import Counter

# optimize


def separateDigits1(self, nums: List[int]) -> List[int]:
    ans = []
    for num in nums:
        a = []
        while num:
            a.append(num % 10)
            num //= 10
        ans.extend(a[::-1])
    return ans

