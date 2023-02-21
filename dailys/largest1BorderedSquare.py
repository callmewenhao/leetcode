# -*- coding: utf-8 -*-

"""
@File    : largest1BorderedSquare.py
@Author  : wenhao
@Time    : 2023/2/17 18:18
@LC      : 1139
"""
from typing import List
from itertools import accumulate


class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        rs = [list(accumulate(row, initial=0)) for row in grid]  # 每一行的前缀和
        cs = [list(accumulate(col, initial=0)) for col in zip(*grid)]  # 每一列的前缀和

        for d in range(min(m, n), 0, -1):
            for i in range(m - d + 1):
                for j in range(n - d + 1):  # 枚举正方形左上角坐标 (i, j)
                    # 上下左右 四条边 1 的个数均为 d
                    if rs[i][j + d] - rs[i][j] == d and \
                            cs[j][i + d] - cs[j][i] == d and \
                            rs[i + d - 1][j + d] - rs[i + d - 1][j] == d and \
                            cs[j + d - 1][i + d] - cs[j + d - 1][i] == d:

                        return d * d
        return 0
