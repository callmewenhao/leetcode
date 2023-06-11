# -*- coding: utf-8 -*-

"""
@File    : minimumTotalPrice.py
@Author  : wenhao
@Time    : 2023/3/27 9:10
@LC      : 
"""
from typing import List
from collections import deque


class Solution:
    # 拓扑排序 😁
    # 性质 如果所有叶子上的金币都收集到了 那么可以顺路把不在叶子上的金币收集到
    # 算法 再次拓扑排序 去掉两轮叶子
    def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:
        n = len(coins)
        g = [[] for _ in range(n)]
        deg = [0] * n  # 节点的度
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
            deg[x] += 1
            deg[y] += 1

        left_edges = n - 1
        # 拓扑排序的的代码
        q = deque()
        for i, (d, c) in enumerate(zip(deg, coins)):
            if d == 1 and c == 0:  # 没有金币的叶子  无向图中的叶子度为 1
                q.append(i)
        # 排序
        while q:
            x = q.popleft()  # 拿出队列中的节点
            left_edges -= 1
            for y in g[x]:  # 把其子节点度减 1
                deg[y] -= 1
                if deg[y] == 1 and coins[y] == 0:  # 继续找没有金币的叶子节点
                    q.append(y)

        # 再跑两轮 拓扑排序 其实就是 bfs 不算是 拓扑排序
        for i, (d, c) in enumerate(zip(deg, coins)):
            if d == 1 and c:  # 有金币的叶子
                q.append(i)
        left_edges -= len(q)
        for x in q:  # 遍历这些有金币的叶子
            for y in g[x]:  # 遍历这些叶子的邻居
                deg[y] -= 1
                if deg[y] == 1:
                    left_edges -= 1

        return max(left_edges * 2, 0)
