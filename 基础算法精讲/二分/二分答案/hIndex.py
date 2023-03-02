# -*- coding: utf-8 -*-

"""
@File    : hIndex.py
@Author  : wenhao
@Time    : 2023/2/15 22:44
@LC      : 274 经典二分答案
"""
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)

        def check(i: int) -> bool:
            return citations[i] >= i + 1

        l, r = 0, len(citations) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if check(mid):
                l = mid + 1
            else:
                r = mid - 1
        return r + 1

