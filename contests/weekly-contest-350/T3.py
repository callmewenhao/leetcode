# -*- coding: utf-8 -*-

"""
@File    : T3.py
@Author  : wenhao
@Time    : 2023/6/18 11:21
@LC      : 
"""
from typing import List
from functools import cache


class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        n = len(nums)
        graph = [[] for _ in range(n)]
        for i, val in enumerate(nums):
            for j in range(i + 1, n):
                if val % nums[j] == 0 or nums[j] % val == 0:
                    graph[i].append(j)
                    graph[j].append(i)
        @cache
        def dfs(x: int, mask: int) -> int:
            if mask == ((1 << n) - 1):
                return 1
            res = 0
            for y in graph[x]:
                if (mask >> y) & 1 == 0:
                    res += dfs(y, mask | (1 << y))
            return res
        ans = 0
        for i in range(n):
            ans += dfs(i, 0 | (1 << i))
            ans %= (10 ** 9 + 7)
        return ans
