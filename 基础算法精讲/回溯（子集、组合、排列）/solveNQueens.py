# -*- coding: utf-8 -*-

"""
@File    : solveNQueens.py
@Author  : wenhao
@Time    : 2023/2/1 0:13
@LC      : 51
"""
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        col = [0] * n

        def valid(r, c):
            for R in range(r):
                C = col[R]
                if r + c == R + C or r - c == R- C:
                    return False
            return True

        def dfs(r: int, s):
            if r == n:
                ans.append(['.' * c + 'Q' + '.' *(n - c - 1) for c in col])
                return
            for c in s:
                if valid(r, c):
                    col[r] = c
                    dfs(r + 1, s - {c})
        dfs(0, set(range(n)))
        return ans
