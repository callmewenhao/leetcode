# -*- coding: utf-8 -*-

"""
@File    : countBattleships.py
@Author  : wenhao
@Time    : 2023/3/3 11:19
@LC      : 419
"""
from typing import List


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        ans = 0
        for i, row in enumerate(board):
            for j, ch in enumerate(row):
                if ch == 'X':
                    ans += 1
                    if i > 0 and board[i - 1][j] == 'X':
                        ans -= 1
                    if j > 0 and board[i][j - 1] == 'X':
                        ans -= 1
        return ans
