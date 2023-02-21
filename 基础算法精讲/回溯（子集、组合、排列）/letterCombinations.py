# -*- coding: utf-8 -*-

"""
@File    : letterCombinations.py
@Author  : wenhao
@Time    : 2023/1/31 20:47
@LC      : 17
"""
from typing import List

MAP = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        ans = []
        if n == 0:
            return ans

        path = [''] * n

        def dfs(i: int):
            if i == n:
                ans.append(''.join(path))
                return
            for ch in MAP[int(digits[i])]:
                path[i] = ch
                dfs(i + 1)

        dfs(0)
        return ans
