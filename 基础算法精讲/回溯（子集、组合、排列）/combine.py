# -*- coding: utf-8 -*-

"""
@File    : combine.py
@Author  : wenhao
@Time    : 2023/1/31 22:38
@LC      : 77
"""
from typing import List


class Solution:
    # for 循环的写法 枚举选哪个
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        path = []

        def dfs(i: int, d: int):
            if len(path) == k:
                ans.append(path.copy())
                return
            for j in range(i, d - 1, -1): # l灵神的optimize
                path.append(j)
                dfs(j - 1, d - 1)
                path.pop()
        dfs(n, k)
        return ans

    # 选或者不选的写法
    def combine1(self, n: int, k: int) -> List[List[int]]:
        ans = []
        path = []

        def dfs(i: int, d: int):
            if len(path) == k:
                ans.append(path.copy())
                return
            if i < d:
                return
            # 选或者不选
            dfs(i - 1, d)
            path.append(i)
            dfs(i - 1, d - 1)
            path.pop()

        dfs(n, k)
        return ans
