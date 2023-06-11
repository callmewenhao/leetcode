# -*- coding: utf-8 -*-

"""
@File    : T2.py
@Author  : wenhao
@Time    : 2023/5/7 14:19
@LC      : 
"""
from typing import List
from collections import Counter
from itertools import accumulate, pairwise
from functools import cache
from math import inf

class Solution:
    def rampartDefensiveLine(self, rampart: List[List[int]]) -> int:
        intervals = [inf] + [x2 - y1 for (x1, y1), (x2, y2) in pairwise(rampart)] + [inf]
        print(intervals)

        def check(val: int) -> bool:
            last_dif = 0
            for interval1, interval2 in pairwise(intervals):
                if interval1 - last_dif + interval2 < val:
                    return False
                last_dif = max(0, val - (interval1 - last_dif))
            return True

        left = min(intervals)
        right = 10**8
        while left <= right:
            mid = left + (right - left) // 2
            if check(mid):
                left = mid + 1
            else:
                right = mid - 1
        return right



