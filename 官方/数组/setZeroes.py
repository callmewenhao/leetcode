# -*- coding: utf-8 -*-

"""
@File    : setZeroes.py
@Author  : wenhao
@Time    : 2023/3/5 15:01
@LC      : 73
"""
from typing import List


class Solution:
    # 优化 使用 O1 的空间
    # 使用两个标记变量记录 第一列 第一行是否含 0
    # 然后使用第一列 第一行记录 其余行列 是否含有 0
    def setZeroes1(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])

        r0 = c0 = False
        for j in range(n):
            if matrix[0][j] == 0:
                r0 = True
                break
        for i in range(m):
            if matrix[i][0] == 0:
                c0 = True
                break
        # 处理第一行 和 第一列
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
        # 改
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if r0:
            for j in range(n):
                matrix[0][j] = 0
        if c0:
            for i in range(m):
                matrix[i][0] = 0

    # m + n 的空间复杂度
    # m 大小的数组表示 哪一行有 0
    # n 大小的数组表示 哪一列有 0
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])

        rows = [False] * m
        cols = [False] * n
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows[i] = True
                    cols[j] = True
        # 改原数组
        for i in range(m):
            if rows[i]:
                for j in range(n):
                    matrix[i][j] = 0
        for j in range(n):
            if cols[j]:
                for i in range(m):
                    matrix[i][j] = 0









