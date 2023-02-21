# -*- coding: utf-8 -*-

"""
@File    : numberOfPaths.py
@Author  : wenhao
@Time    : 2023/1/6 23:00
"""
from typing import List


class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        ans = 0
        MOD = 10 ** 9 + 7
        m, n = len(grid), len(grid[0])
        f = [[[0] * k for _ in range(n + 1)] for _ in range(m + 1)]
        f[0][1][0] = 1



        return ans

