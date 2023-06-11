# -*- coding: utf-8 -*-

"""
@File    : T2.py
@Author  : wenhao
@Time    : 2023/5/28 10:24
@LC      : 
"""
from typing import List
from math import inf
from functools import cache
from itertools import accumulate
from collections import Counter


class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ans = [[0] * n for _ in range(m)]

        for j in range(n):
            cnt1 = Counter()
            x, y = 0, j
            while x < m and y < n:
                cnt1[grid[x][y]] += 1
                x += 1
                y += 1

            cnt2 = Counter()
            x, y = 0, j
            while x < m and y < n:
                cnt1[grid[x][y]] -= 1
                if cnt1[grid[x][y]] == 0:
                    cnt1.pop(grid[x][y])
                if 0 < x:
                    cnt2[grid[x - 1][y - 1]] += 1
                ans[x][y] = abs(len(cnt1) - len(cnt2))
                x += 1
                y += 1

        for i in range(1, m):
            cnt1 = Counter()
            x, y = i, 0
            while x < m and y < n:
                cnt1[grid[x][y]] += 1
                x += 1
                y += 1

            cnt2 = Counter()
            x, y = i, 0
            while x < m and y < n:
                cnt1[grid[x][y]] -= 1
                if cnt1[grid[x][y]] == 0:
                    cnt1.pop(grid[x][y])
                if y > 0:
                    cnt2[grid[x - 1][y - 1]] += 1
                ans[x][y] = abs(len(cnt1) - len(cnt2))
                x += 1
                y += 1

        return ans
