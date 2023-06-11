# -*- coding: utf-8 -*-

"""
@File    : minimumTotalPrice.py
@Author  : wenhao
@Time    : 2023/4/15 22:59
@LC      : 
"""
from typing import List
from math import inf
from functools import cache
from itertools import accumulate
from collections import Counter


class Graph:
    # 朴素 Dijkstra  有堆优化的版本  O(n^2) 时间
    def __init__(self, n: int, edges: List[List[int]]):
        self.g = [[inf] * n for _ in range(n)]
        for x, y, w in edges:
            self.g[x][y] = w

    def addEdge(self, e: List[int]) -> None:
        self.g[e[0]][e[1]] = e[2]

    def shortestPath(self, start: int, end: int) -> int:
        n = len(self.g)
        dis = [inf] * n  # 起点到所有点的最短路
        dis[start] = 0
        vis = [False] * n  # 标记已经被更新成最短路的点

        while True:  # for _ in range(n)
            # 找当前最短路
            x = -1
            for i in range(n):
                if not vis[i] and (x < 0 or dis[i] < dis[x]):
                    x = i
            if x < 0 or dis[x] == inf:  # 不连通
                return -1
            if x == end:  # 找到了
                return dis[x]

            vis[x] = True
            for y, w in enumerate(self.g[x]):
                if dis[x] + w < dis[y]:  # 如果新的路径小于之前算的 就更新
                    dis[y] = dis[x] + w

    # floyd 做法 O(n^3) 时间
    # 定义f[k][i][j]表示除了i和j以外，从i到j的路径中间点上至多为k的时候#从i到j的最短路的长度
    # 分类讨论:
    # 从i到j的最短路中间至多为k-1
    # 从i到j的最短路中间至多为k:说明k一定是中间节点
    # f[k][i][j]= min(f[k-1][i][j]，f[k-1][i][K] + f[k-1][k][j])
    # f[i][j]= min(f[i][j]，f[i][k] + f[k][j])
    def __init__(self, n: int, edges: List[List[int]]):
        g = [[inf] * n for _ in range(n)]
        for x, y, w in edges:
            g[x][y] = w
        for i in range(n):
            g[i][i] = 0
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if g[i][k] + g[k][j] < g[i][j]:
                        g[i][j] = g[i][k] + g[k][j]
                    # g[i][j] = min(g[i][j], g[i][k] + g[k][j])
        self.g = g

    def addEdge(self, e: List[int]) -> None:
        # O(n^2)
        g = self.g  # 注意这是个指针（引用）
        n = len(g)
        x, y, w = e
        if w >= g[x][y]:  # 无效更新
            return
        g[x][y] = w
        for i in range(n):
            for j in range(n):  # 更新
                if (s := g[i][x] + g[x][y] + g[y][j]) < g[i][j]:
                    g[i][j] = s
                # g[i][j] = min(g[i][j], g[i][x] + g[x][y] + g[y][j])

    def shortestPath(self, start: int, end: int) -> int:
        # O(1) 回答询问
        dis = self.g[start][end]
        return dis if dis < inf else -1

# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)
