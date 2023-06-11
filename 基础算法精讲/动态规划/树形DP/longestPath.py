# -*- coding: utf-8 -*-

"""
@File    : longestPath.py
@Author  : wenhao
@Time    : 2023/4/17 23:08
@LC      : 2246
"""
from typing import List


class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        # 建树 只有 n 条边就使用邻接表
        n = len(parent)
        g = [[] for _ in range(n)]
        for i in range(1, n):
            g[parent[i]].append(i)

        ans = 0
        def dfs(x) -> int:
            nonlocal ans
            x_len = 0
            for y in g[x]:
                y_len = dfs(y) + 1
                if s[y] != s[x]:
                    ans = max(ans, x_len + y_len)
                    x_len = max(x_len, y_len)
            return x_len
        dfs(0)
        return ans + 1  # 这里要求点的数量








