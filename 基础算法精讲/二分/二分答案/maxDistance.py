# -*- coding: utf-8 -*-

"""
@File    : maxDistance.py
@Author  : wenhao
@Time    : 2023/2/10 21:22
@LC      : 1552
"""
from typing import List


class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        def check(mi: int) -> bool:
            cnt = 1
            p0 = position[0]
            for i in range(1, len(position)):
                if position[i] >= p0 + mi:
                    cnt += 1
                    p0 = position[i]
            return cnt >= m
        l, r = 1, (position[-1] - position[0]) // (m - 1)
        while l <= r:
            mid = l + (r - l) // 2
            if check(mid):
                l = mid + 1
            else:
                r = mid - 1
        return r  # or l - 1









