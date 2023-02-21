# -*- coding: utf-8 -*-

"""
@File    : combinationSum3.py
@Author  : wenhao
@Time    : 2023/1/31 22:57
@LC      : 216
"""
from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        path = []

        def dfs(i: int, t: int):
            d = k - len(path)
            if t < 0 or t > (2 * i - d  + 1) * d// 2:
                return
            if len(path) == k:
                ans.append(path.copy())
                return
            for j in range(i, d - 1, -1):  # l灵神的optimize
                path.append(j)
                dfs(j - 1, t - j)
                path.pop()

        dfs(9, n)
        return ans
