# -*- coding: utf-8 -*-

"""
@File    : matrixReshape.py
@Author  : wenhao
@Time    : 2023/3/4 23:06
@LC      : 566
"""
from typing import List


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        if m * n != r * c:  # 如果输入参数不对 就返回原数组
            return mat

        ans = [[0] * c for _ in range(r)]
        for i in range(m):
            for j in range(n):
                idx = i * n + j
                x = idx // c
                y = idx - x * c
                ans[x][y] = mat[i][j]
        return ans
