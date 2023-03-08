# -*- coding: utf-8 -*-

"""
@File    : generateMatrix.py
@Author  : wenhao
@Time    : 2023/3/4 14:23
@LC      : 59
"""
from typing import List


class Solution:
    # 思路就是 54 题目的反向
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0] * n for _ in range(n)]

        x, y, d = 0, 0, 0
        offset = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        for i in range(1, n * n + 1):
            ans[x][y] = i

            x_ = x + offset[d][0]
            y_ = y + offset[d][1]

            if not (0 <= x_ < n and 0 <= y_ < n) or ans[x_][y_] != 0:
                d = (d + 1) % 4
                x_ = x + offset[d][0]
                y_ = y + offset[d][1]
            x = x_
            y = y_
        return ans