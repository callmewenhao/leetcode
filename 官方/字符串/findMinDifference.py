# -*- coding: utf-8 -*-

"""
@File    : findMinDifference.py
@Author  : wenhao
@Time    : 2023/3/13 14:10
@LC      : 539
"""
from typing import List
from itertools import pairwise


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        mins = [60 * int(t[0:2]) + int(t[3:]) for t in timePoints]
        mins.sort()
        mi = min(e - s for s, e in pairwise(mins))
        return min(mi, 24 * 60 + mins[0] - mins[-1])  # 处理首尾元素


