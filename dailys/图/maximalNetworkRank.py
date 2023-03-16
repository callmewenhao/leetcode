# -*- coding: utf-8 -*-

"""
@File    : maximalNetworkRank.py
@Author  : wenhao
@Time    : 2023/3/15 9:24
@LC      : 1615
"""
from typing import List


class Solution:
    # 认真分析问题 😁
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = [[0] * n for _ in range(n)]
        for x, y in roads:
            graph[x][y] = 1
            graph[y][x] = 1

        ans = 0
        s = [sum(r) for r in graph]
        for i in range(n):
            for j in range(i + 1, n):
                ans = max(ans, s[i] + s[j] - (1 if graph[i][j] else 0))
        return ans
