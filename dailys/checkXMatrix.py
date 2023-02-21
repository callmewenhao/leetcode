# -*- coding: utf-8 -*-

"""
@File    : checkXMatrix.py
@Author  : wenhao
@Time    : 2023/1/31 10:18
@LC      : 2319
"""
from typing import List


class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        for i in range(n):
            if grid[i][i] == 0 or grid[i][n - 1 - i] == 0:
                return False
            for j in range(n):
                if j != i and j != n - 1 - i and grid[i][j] != 0:
                    return False
        return True
