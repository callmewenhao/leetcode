# -*- coding: utf-8 -*-

"""
@File    : 1079numTilePossibilities.py
@Author  : wenhao
@Time    : 2023/5/19 15:38
@LC      : 1079
"""
from math import comb, perm
from collections import Counter


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        counts = list(Counter(tiles).values())
        n, m = len(tiles), len(counts)

        f = [[0] * (n + 1) for _ in range(m + 1)]
        f[0][0] = 1

        for i, cnt in enumerate(counts, 1):
            for j in range(n + 1):
                for k in range(min(j, cnt) + 1):
                    f[i][j] += f[i-1][j-k] * comb(j, k)
        return sum(f[m][1:])
