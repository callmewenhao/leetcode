# -*- coding: utf-8 -*-

"""
@File    : spiralOrder.py
@Author  : wenhao
@Time    : 2023/3/4 10:48
@LC      : 54
"""
from typing import List


class Solution:
    # 分析
    # 答案长度 mn
    # 模拟整个遍历过程
    # 一共四个方向 offset = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    # 在出现冲突时进行方向调整 if not (0 <= x_ < m and 0 <= y_ < n) or matrix[x_][y_] == 101:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])

        ans = [0] * (m * n)
        x, y, d = 0, 0, 0
        offset = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        for i in range(m * n):
            ans[i] = matrix[x][y]
            matrix[x][y] = 101

            x_ = x + offset[d][0]
            y_ = y + offset[d][1]

            if not (0 <= x_ < m and 0 <= y_ < n) or matrix[x_][y_] == 101:
                d = (d + 1) % 4
                x_ = x + offset[d][0]
                y_ = y + offset[d][1]

            x = x_
            y = y_

        return ans
