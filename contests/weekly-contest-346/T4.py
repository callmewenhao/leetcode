# -*- coding: utf-8 -*-

"""
@File    : T4.py
@Author  : wenhao
@Time    : 2023/6/9 10:05
@LC      : 2699
"""

from typing import List
from math import inf
from functools import cache
from itertools import accumulate
from collections import Counter


class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        g = [[] for _ in range(n)]
        for i, (x, y, _) in enumerate(edges):
            g[x].append((y, i))
            g[y].append((x, i))
        dis = [[inf, inf] for _ in range(n)]
        dis[source] = [0, 0]

        def dijkstra(k: int) -> None:  # k 表示第几次
            vis = [False] * n
            while True:
                x = -1
                for y, (b, d) in enumerate(zip(vis, dis)):
                    if not b and (x < 0 or d[k] < dis[x][k]):
                        x = y
                if x == destination:
                    return
                vis[x] = True

                for y, eid in g[x]:
                    wt = edges[eid][2]
                    if wt == -1:
                        wt = 1
                    if k == 1 and edges[eid][2] == -1:
                        w = delta + dis[y][0] - dis[x][1]
                        if w > wt:
                            edges[eid][2] = wt = w
                    dis[y][k] = min(dis[y][k], dis[x][k] + wt)

        dijkstra(0)
        delta = target - dis[destination][0]
        if delta < 0:
            return []

        dijkstra(1)
        if dis[destination][1] < target:
            return []

        for e in edges:
            if e[2] == -1:
                e[2] = 1

        return edges




































