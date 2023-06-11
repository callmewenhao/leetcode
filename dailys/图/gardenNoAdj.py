# -*- coding: utf-8 -*-

"""
@File    : gardenNoAdj.py
@Author  : wenhao
@Time    : 2023/4/15 20:54
@LC      : 1042
"""
from typing import List


class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        g = [[] for _ in range(n)]
        for x, y in paths:
            g[x - 1].append(y - 1)
            g[y - 1].append(x - 1)
        color = [0] * n
        for i, nodes in enumerate(g):
            color[i] = (set(range(1, 5)) - {color[j] for j in nodes}).pop()
        return color








