# -*- coding: utf-8 -*-

"""
@File    : numMovesStonesII.py
@Author  : wenhao
@Time    : 2023/4/7 16:16
@LC      : 1040
"""
from typing import List


class Solution:
    def numMovesStonesII(self, s: List[int]) -> List[int]:
        s.sort()
        n = len(s)
        e1 = s[-2] - s[0] - n + 2
        e2 = s[-1] - s[1] - n + 2

        max_move = max(e1, e2)
        if e1 == 0 or e2 == 0:
            return [min(2, max_move), max_move]

        max_cnt = left = 0
        for right, x in enumerate(s):
            while s[left] <= x - n:
                left += 1
            max_cnt = max(max_cnt, right - left + 1)
        return [n - max_cnt, max_move]
