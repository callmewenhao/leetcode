# -*- coding: utf-8 -*-

"""
@File    : T3.py
@Author  : wenhao
@Time    : 2023/5/14 10:23
@LC      : 
"""

from typing import List
from math import inf
from functools import cache
from itertools import accumulate
from collections import Counter


class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        offset = [[-1, 1], [0, 1], [1, 1]]
        ans = 0
        for i in range(m):
            # [i, 0]
            g = grid.copy()
            cnt = 0
            qu = [[i, 0]]
            g[i][0] *= -1

            while len(qu):
                nqu = []
                for x, y in qu:
                    val = abs(g[x][y])
                    for dx, dy in offset:
                        nx, ny = x + dx, y + dy
                        if nx < 0 or ny < 0 or nx >= m or ny >= n:
                            continue
                        if g[nx][ny] > 0 and g[nx][ny] > val:
                            nqu.append([nx, ny])
                            g[nx][ny] *= -1
                cnt += 1
                qu = nqu
            ans = max(ans, cnt)
        return ans
