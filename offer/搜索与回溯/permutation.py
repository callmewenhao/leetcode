# -*- coding: utf-8 -*-

"""
@File    : permutation.py
@Author  : wenhao
@Time    : 2023/2/17 19:44
@LC      : 
"""
from typing import List
from string import ascii_lowercase

class Solution:
    def permutation(self, s: str) -> List[str]:

        ans = []
        path = []
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch)] += 1

        n = len(s)
        vis = [False] * n

        def dfs(i: int):
            nonlocal path
            path.append(ascii_lowercase[i])
            cnt[i] -= 1

            if len(path) == n:
                ans.append("".join(path))
                return

            for j in range(n):
                if vis[j]:
                    continue
                dfs(j)

            path.pop()
            vis[i] = False

        for i in range(26):
            if cnt[i]:
                dfs(i)
        return ans












