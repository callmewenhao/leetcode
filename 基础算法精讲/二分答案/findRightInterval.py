# -*- coding: utf-8 -*-

"""
@File    : findRightInterval.py
@Author  : wenhao
@Time    : 2023/2/19 22:22
@LC      : 436
"""
from typing import List
from bisect import bisect_left

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        for i, interval in enumerate(intervals):
            interval.append(i)
        intervals.sort()

        n = len(intervals)
        ans = [-1] * n

        for _, end, id in intervals:
            i = bisect_left(intervals, [end])
            if i < n:
                ans[id] = intervals[i][2]
        return ans












