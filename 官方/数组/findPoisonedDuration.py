# -*- coding: utf-8 -*-

"""
@File    : findPoisonedDuration.py
@Author  : wenhao
@Time    : 2023/2/4 21:09
@LC      : 495
"""
from typing import List


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        ans = 0
        end = -1
        for t in timeSeries:
            if end < t:
                ans += duration
            else:
                ans += (t + duration - 1) - end
            end = t + duration - 1
        return ans