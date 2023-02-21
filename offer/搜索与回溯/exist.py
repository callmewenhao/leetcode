# -*- coding: utf-8 -*-

"""
@File    : exist.py
@Author  : wenhao
@Time    : 2023/1/31 10:30
@LC      : offer 12
"""
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        vis = [[False] * n for _ in range(m)]

        def dfs(x, y, i) -> bool:
            if i == len(word):
                return True
            if x < 0 or y < 0 or x >= m or y >= n:
                return False
            if vis[x][y] or board[x][y] != word[i]:
                return False
            vis[x][y] = True
            if dfs(x + 1, y, i + 1) or \
                   dfs(x - 1, y, i + 1) or \
                   dfs(x, y - 1, i + 1) or \
                   dfs(x, y + 1, i + 1):
                return True

            vis[x][y] = False
            return False

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True

        return False
