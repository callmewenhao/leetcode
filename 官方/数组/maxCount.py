# -*- coding: utf-8 -*-

"""
@File    : maxCount.py
@Author  : wenhao
@Time    : 2023/3/3 10:53
@LC      : 598
"""
from typing import List


class Solution:
    # 脑筋急转弯 😁
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        x, y = m, n
        for _x, _y in ops:
            x = min(x, _x)
            y = min(y, _y)
        return x * y