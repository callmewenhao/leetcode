# -*- coding: utf-8 -*-

"""
@File    : spiralOrder.py
@Author  : wenhao
@Time    : 2023/2/16 16:32
@LC      : 
"""
from typing import List


class Solution:
    # 指导思想：分类讨论
    # 先右后下、先下后左、先左后上、先上后右 完美闭环😊
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        ans = []

        def run(x, y):
            ans.append(matrix[x][y])
            matrix[x][y] = 101
            if 0 <= x - 1 < m and matrix[x - 1][y] != 101:
                if 0 <= y - 1 < n and matrix[x][y - 1] != 101:
                    run(x, y - 1)
                else:
                    run(x - 1, y)
            if 0 <= x + 1 < m and matrix[x + 1][y] != 101:
                if 0 <= y + 1 < n and matrix[x][y + 1] != 101:
                    run(x, y + 1)
                else:
                    run(x + 1, y)
            if 0 <= y + 1 < n and matrix[x][y + 1] != 101:
                if 0 <= x - 1 < n and matrix[x - 1][y] != 101:
                    run(x - 1, y)
                else:
                    run(x, y + 1)
            if 0 <= y - 1 < n and matrix[x][y - 1] != 101:
                if 0 <= x + 1 < m and matrix[x + 1][y] != 101:
                    run(x + 1, y)
                else:
                    run(x, y - 1)
        run(0, 0)
        return ans

