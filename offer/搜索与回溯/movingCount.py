# -*- coding: utf-8 -*-

"""
@File    : movingCount.py
@Author  : wenhao
@Time    : 2023/1/31 11:09
@LC      : 面试题 13
"""


class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        ans = 0
        vis = [[False] * n for _ in range(m)]

        def bitSum(x: int, y: int) -> int:
            ans = 0
            while x:
                ans += x % 10
                x //= 10
            while y:
                ans += y % 10
                y //= 10
            return ans

        def dfs(x: int, y: int):
            nonlocal ans
            if x < 0 or x >= m or y < 0 or y >= n:
                return
            if vis[x][y] or bitSum(x, y) > k:
                return
            vis[x][y] = True
            ans += 1
            dfs(x - 1, y)
            dfs(x + 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)

        dfs(0, 0)
        return ans
