# -*- coding: utf-8 -*-

"""
@File    : findRightInterval.py
@Author  : wenhao
@Time    : 2023/2/19 21:52
@LC      : 436
"""
from typing import List


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        a = sorted(enumerate(intervals), key=lambda x: x[1][0])
        idx = [x[0] for x in a]

        n = len(idx)
        ans = [0] * n
        for i, id in enumerate(idx):
            s, e = intervals[id]

            l, r = i + 1, n - 1
            while l <= r:
                mid = l + (r - l) // 2
                if intervals[idx[mid]][0] < e:
                    l = mid + 1
                if intervals[idx[mid]][0] >= e:
                    r = mid - 1
            ans[i] = idx[l] if l < n else -1
        return ans




