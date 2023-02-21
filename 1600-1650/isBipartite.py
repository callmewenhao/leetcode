# -*- coding: utf-8 -*-

"""
@File    : isBipartite.py
@Author  : wenhao
@Time    : 2023/2/1 20:13
@LC      : 785
"""
from typing import List
from collections import deque

class Solution:
    # bfs
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        vis = [False] * n
        color = [0] * n

        dq = deque()
        for i in range(n):
            if vis[i]:
                continue
            dq.append(i)

            vis[i] = True
            color[i] = 1

            while len(dq):
                node = dq.popleft()
                for j in graph[node]:
                    if vis[j] and color[j] == color[node]:
                        return False
                    if not vis[j]:
                        vis[j] = True
                        color[j] = -color[node]
                        dq.append(j)
        return True

    # dfs optimize
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        vis = [False] * n
        color = [0] * n

        def dfs(i: int, c: int) -> bool:
            if vis[i]:
                return color[i] == c

            vis[i] = True
            color[i] = c
            for j in graph[i]:
                if not dfs(j, -c):
                    return False

            return True

        for i in range(n):
            if not vis[i] and not dfs(i, 1):
                return False
        return True

    # dfs
    def isBipartite1(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        vis = [False] * n
        color = [0] * n

        def dfs(i: int, c: int) -> bool:
            vis[i] = True
            color[i] = c

            for j in graph[i]:
                if vis[j] and color[j] == c:
                    return False
                elif not vis[j] and not dfs(j, -c):
                    return False
            return True

        for i in range(n):
            if not vis[i] and not dfs(i, 1):
                return False
        return True
