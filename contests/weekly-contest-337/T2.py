# -*- coding: utf-8 -*-

"""
@File    : T2.py
@Author  : wenhao
@Time    : 2023/3/19 10:20
@LC      : 
"""
from typing import List
from collections import Counter
from itertools import pairwise


class Solution:
    # 灵神思路更妙
    # 统计 每个数所在的位置 然后判断相邻的数之前的 x y 之差是否符合要求
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        pos = [None] * (len(grid) ** 2)
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                pos[x] = (i, j)
        if pos[0] != (0, 0):
            return False
        for (i, j), (x, y) in pairwise(pos):
            dx = abs(x - i)
            dy = abs(y - j)
            if (dx != 2 or dy != 1) and (dx != 1 or dy != 2):
                return False
        return True

    def checkValidGrid1(self, grid: List[List[int]]) -> bool:
        d = [[1, -2], [2, -1], [2, 1], [1, 2],
             [-1, 2], [-2, 1], [-2, -1], [-1, -2]]
        x = y = 0
        n = len(grid)
        cnt = 1
        while True:
            x_ = y_ = 0
            for dx, dy in d:
                x_ = x + dx
                y_ = y + dy
                if 0 <= x_ < n and 0 <= y_ < n and grid[x_][y_] == cnt:
                    cnt += 1
                    break
            if not (0 <= x_ < n and 0 <= y_ < n) or grid[x_][y_] != grid[x][y] + 1:
                break
            x, y = x_, y_

        return cnt == n * n
