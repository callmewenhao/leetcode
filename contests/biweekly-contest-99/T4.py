# -*- coding: utf-8 -*-

"""
@File    : T4.py
@Author  : wenhao
@Time    : 2023/3/5 20:23
@LC      : 
"""

"""
1. 把以 0 根的猜对次数算出来 cnt0 使用一个 DFS
2. 再跑一次 DFS

cnt
0 -> 1
cnt - (0,1) in s + (1, 0) in s

进阶：bob 猜测树中 u 是 v 的祖先节点
还是看 灵神 视频吧

"""
from typing import List


class Solution:
    def rootCount(self, edges: List[List[int]], guesses: List[List[int]], k: int) -> int:
        # 建图
        g = [[] for _ in range(len(edges) + 1)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
        # 把 guesses 转成 hashmap
        s = {(x, y) for x, y in guesses}

        # 以 0 为根时的正确猜测数目
        cnt0 = 0
        def dfs(x: int, fa: int) -> None:
            nonlocal cnt0
            for y in g[x]:
                if y != fa:
                    if (x, y) in s:
                        cnt0 += 1
                    dfs(y, x)
        dfs(0, -1)

        # 算答案
        ans = 0
        def reroot(x: int, fa: int, cnt: int) -> None:
            # cnt 表示以 x 为根猜对的次数
            nonlocal ans
            if cnt >= k:
                ans += 1
            for y in g[x]:
                if y != fa:
                    reroot(y, x, cnt -((x, y) in s) + ((y, x) in s))
        reroot(0, -1, cnt0)
        return ans




