# -*- coding: utf-8 -*-

"""
@File    : maxArea.py
@Author  : wenhao
@Time    : 2023/1/29 22:48
"""
from typing import List


class Solution:
    def maxArea(self, h: List[int]) -> int:
        ans = 0
        n = len(h)
        l, r = 0, n - 1
        while l < r:
            area = (r - l) * min(h[l], h[r])
            ans = max(ans, area)
            if h[l] < h[r]:
                l += 1
            else:
                r -= 1
        return ans
