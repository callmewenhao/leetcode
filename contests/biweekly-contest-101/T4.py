# -*- coding: utf-8 -*-

"""
@File    : minimumTotalPrice.py
@Author  : wenhao
@Time    : 2023/4/3 9:51
@LC      : 
"""

"""
图中最短环 经典图论题目😂
环：从点 a 到点 b，有两条不同的简单路径，这两条简单路径就组成了一个环

BFS 枚举起点 start 
如果找到两条从 start 出发的不同的简单路径 能够到达同一个点
那么当前这个环就是最小的 后面继续找 只能找到更大的

实现上的技巧
用一个数组记录从 start 出发的最短路的长度
队列中还需记录上一个点 防止重复访问
"""

from typing import List
from collections import deque
from math import inf


class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        # 建图
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        def bfs(start: int) -> int:
            dis = [-1] * n  # dis[i] 表示 start 到 i 的最短路
            dis[start] = 0
            q = deque([(start, -1)])  # 元素是一个()
            while q:
                x, fa = q.popleft()
                for y in g[x]:
                    if dis[y] < 0:
                        dis[y] = dis[x] + 1
                        q.append((y, x))
                    elif y != fa:
                        return dis[x] + dis[y] + 1  # 找到的最小环
            return 1001  # inf

        ans = min(bfs(i) for i in range(n))
        return ans if ans < 1001 else -1




