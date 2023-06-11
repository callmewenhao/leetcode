# -*- coding: utf-8 -*-

"""
@File    : T1.py
@Author  : wenhao
@Time    : 2023/4/15 22:24
@LC      : 
"""
from typing import List
from collections import Counter


class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        ans = []
        for col in zip(*grid):
            mx = 0
            for x in col:
                mx = max(mx, len(str(x)))
            ans.append(mx)
        return ans

    def findColumnWidth1(self, grid: List[List[int]]) -> List[int]:
        m = len(grid)
        n = len(grid[0])

        ans = [0] * n
        for j in range(n):
            for i in range(m):
                ans[j] = max(len(str(grid[i][j])), ans[j])
        return ans
