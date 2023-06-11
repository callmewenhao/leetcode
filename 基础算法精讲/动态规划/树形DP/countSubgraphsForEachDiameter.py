# -*- coding: utf-8 -*-

"""
@File    : countSubgraphsForEachDiameter.py
@Author  : wenhao
@Time    : 2023/4/18 10:07
@LC      : 1617
"""
from typing import List


class Solution:
    # 当边的个数小于 n 时 邻接表是最好的选择
    # 二进制枚举优化
    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
        # 建树
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x - 1].append(y - 1)
            g[y - 1].append(x - 1)  # 编号从 0 开始

        ans = [0] * (n - 1)
        for mask in range(3, 1 << n):  # 3==0011
            if (mask & (mask - 1)) == 0:  # 至少需要一个点
                continue
            diameter = vis = 0

            # 求树的直径
            def dfs(x: int) -> int:
                nonlocal diameter, vis
                vis |= 1 << x  # 标记 x 访问过
                max_len = 0
                for y in g[x]:
                    if (vis >> y & 1) == 0 and mask >> y & 1:
                        ml = dfs(y) + 1
                        diameter = max(diameter, max_len + ml)
                        max_len = max(max_len, ml)
                return max_len
            dfs(mask.bit_count() - 1)  # 从一个在 mask 中的点开始递归
            if vis == mask:
                ans[diameter - 1] += 1
        return ans

    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
        # 建树
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x - 1].append(y - 1)
            g[y - 1].append(x - 1)  # 编号从 0 开始

        ans = [0] * (n - 1)
        in_set = [False] * n

        def f(i: int) -> None:
            if i == n:
                vis = [False] * n
                diameter = 0
                for v, b in enumerate(in_set):
                    if not b: continue

                    # 求树的直径
                    def dfs(x: int) -> int:
                        nonlocal diameter
                        vis[x] = True
                        max_len = 0
                        for y in g[x]:
                            if not vis[y] and in_set[y]:
                                ml = dfs(y) + 1
                                diameter = max(diameter, max_len + ml)
                                max_len = max(max_len, ml)
                        return max_len

                    dfs(v)
                    break  # 只用找一个点就行
                if diameter and vis == in_set:
                    ans[diameter - 1] += 1
                return

            # 不选城市 i
            f(i + 1)
            # 选城市 i
            in_set[i] = True
            f(i + 1)
            in_set[i] = False  # 恢复现场

        f(0)
        return ans
