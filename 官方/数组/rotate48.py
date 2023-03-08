# -*- coding: utf-8 -*-

"""
@File    : rotate48.py
@Author  : wenhao
@Time    : 2023/3/4 23:23
@LC      : 48
"""
from typing import List


class Solution:
    # 反转矩阵做法
    # 顺时针旋转 90° == 上下反转 + 主对角线反转
    def rotate1(self, matrix: List[List[int]]) -> None:
        # 上下反转
        n = len(matrix)
        i, j = 0, n - 1
        while i < j:
            for col in range(n):
                matrix[i][col], matrix[j][col] = matrix[j][col], matrix[i][col]
            i += 1
            j -= 1

        # 对角线反转
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 建议看题解
        # 图像顺时针转 90 度 其实是对应的 4 个点之间的移动
        # 只要 弄清楚 这 4 个点的移动关系就行 如下
        # n * n: (x, y) -> (y, n-1-x) -> (n-1-x, n-1-y) -> (n-1-y, x) -> (x, y)
        # 下一个问题就是 第一个点的取值范围
        # n 为 偶数 时
        # (x, y) 的取值范围是 (0 - n//2 - 1, 0 - n//2 - 1) 前 1/4 的区域
        # n 为 奇数 时
        # (x, y) 的取值范围是 (0 - n//2 - 1, 0 - (n + 1)//2 - 1) 下取整 上取整
        n = len(matrix)
        for i in range(n // 2):
            for j in range((n + 1) // 2):
                t = matrix[i][j]
                matrix[i][j] = matrix[n - 1 - j][i]
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
                matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
                matrix[j][n - 1 - i] = t
