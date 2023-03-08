# -*- coding: utf-8 -*-

"""
@File    : gameOfLife.py
@Author  : wenhao
@Time    : 2023/3/5 15:29
@LC      : 289
"""
from typing import List


class Solution:
    # 思路 原地做标记
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        for i in range(m):
            for j in range(n):
                cnt = 0
                for x_ in range(-1, 2, 1):
                    for y_ in range(-1, 2, 1):
                        if x_ == 0 and y_ == 0:
                            continue
                        x = i + x_
                        y = j + y_
                        if 0 <= x < m and 0 <= y < n and board[x][y] > 0:
                            cnt += 1
                if board[i][j] == 0 and cnt == 3:
                    board[i][j] = -2
                if board[i][j] == 1 and (cnt < 2 or cnt > 3):
                    board[i][j] = 2
        print(board)

        for i in range(m):
            for j in range(n):
                if board[i][j] == -2:
                    board[i][j] = 1
                if board[i][j] == 2:
                    board[i][j] = 0