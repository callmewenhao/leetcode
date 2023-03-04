# -*- coding: utf-8 -*-

"""
@File    : generate.py
@Author  : wenhao
@Time    : 2023/3/2 22:47
@LC      : 118
"""
from typing import List


class Solution:
    # 二维数组 递推
    def generate1(self, n: int) -> List[List[int]]:
        f = [[0] * (i + 1) for i in range(n)]
        for i, row in enumerate(f):
            for j in range(len(row)):
                if i == j or j == 0:
                    f[i][j] = 1
                else:
                    f[i][j] = f[i - 1][j - 1] + f[i - 1][j]
        return f
