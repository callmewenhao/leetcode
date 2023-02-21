# -*- coding: utf-8 -*-

"""
@File    : partition.py
@Author  : wenhao
@Time    : 2023/1/31 21:19
@LC      : 131
"""
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # python 判断回文
        def isPalin(n: str) -> bool:
            return n == n[::-1]  # 多用切片，少用函数

        ans = []
        path = []
        n = len(s)

        def dfs(i: int):
            if i == n:
                ans.append(path.copy())
                return
            for j in range(i, n):
                if isPalin(s[i:j + 1]):
                    path.append(s[i:j + 1])
                    dfs(j + 1)
                    path.pop()

        dfs(0)
        return ans
