# -*- coding: utf-8 -*-

"""
@File    : maximumEvenSplit.py
@Author  : wenhao
@Time    : 2023/7/6 21:45
@LC      : 
"""
from typing import List
from functools import cache

class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum & 1:
            return []

        ans = []
        x = 2
        while x <= finalSum:
            ans.append(x)
            finalSum -= x
            x += 2
        ans[-1] += finalSum



