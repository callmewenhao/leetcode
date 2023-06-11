# -*- coding: utf-8 -*-

"""
@File    : T4.py
@Author  : wenhao
@Time    : 2023/5/29 22:59
@LC      : 
"""
from typing import List
from math import inf
from functools import cache
from itertools import accumulate
from collections import Counter, defaultdict


class Solution:
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:
        dict = defaultdict(list)
        m, n = len(mat), len(mat[0])
        for i, row in enumerate(mat):
            for j, x in enumerate(row):
                dict[x].append((i, j))

        ans = 0
        row_max = [0] * m
        col_max = [0] * n
        for _, pos in sorted(dict.items(), key=lambda p: p[0]):
            # 先找最大值
            mx = [max(row_max[x], col_max[y]) + 1 for x, y in pos]
            ans = max(ans, max(mx))  # 更新答案
            for (x, y), f in zip(pos, mx):
                row_max[x] = max(f, row_max[x])
                col_max[y] = max(f, col_max[y])
        return ans




