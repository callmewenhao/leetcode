# -*- coding: utf-8 -*-

"""
@File    : isStraight.py
@Author  : wenhao
@Time    : 2023/2/2 11:25
@LC      : 
"""
from typing import List


class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        s = set()
        ma, mi = 0, 14
        for val in nums:
            if val == 0:
                continue
            ma = max(ma, val)
            mi = min(mi, val)
            if val in s:
                return False
            s.add(val)
        return ma - mi < 5
