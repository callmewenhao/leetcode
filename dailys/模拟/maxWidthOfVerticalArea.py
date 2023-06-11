# -*- coding: utf-8 -*-

"""
@File    : maxWidthOfVerticalArea.py
@Author  : wenhao
@Time    : 2023/3/30 9:18
@LC      : 1637
"""
from typing import List
from itertools import pairwise

class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key=lambda p: p[0])
        return max(x2 - x1 for x1, x2 in pairwise(x for x, y in points))






