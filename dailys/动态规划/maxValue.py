# -*- coding: utf-8 -*-

"""
@File    : maxValue.py
@Author  : wenhao
@Time    : 2023/3/8 8:51
@LC      : 
"""
from typing import List
from functools import cache


class Solution:

    # 一维 dp
    def maxValue2(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        # 边界条件就是 f[0] = 0
        f = [0] * (n + 1)
        for i in range(m):
            for j in range(n):
                f[j + 1] = grid[i][j] + max(f[j], f[j + 1])
        return f[n]

    # 二维 dp
    def maxValue1(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        # 边界条件就是 f[0][j] = 0 f[i][0] = 0
        f = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                f[i + 1][j + 1] = grid[i][j] + max(f[i][j + 1], f[i + 1][j])
        return f[m][n]

    # 记忆化搜索
    def maxValue(self, grid: List[List[int]]) -> int:
        @cache
        def dfs(x: int, y: int) -> int:
            # 边界条件
            # 当 x y 任意一个小于 0 时 其能得到的最大值都是 0
            if x < 0 or y < 0:
                return 0
            # 返回 上 左的最大值 + 本位置的值
            return grid[x][y] + max(dfs(x, y - 1), dfs(x - 1, y))

        m = len(grid)
        n = len(grid[0])
        return dfs(m - 1, n - 1)
