# -*- coding: utf-8 -*-

"""
@File    : permutation.py
@Author  : wenhao
@Time    : 2023/2/20 10:37
@LC      : 有重复的全排列问题
"""
from typing import List


class Solution:
    def permutation(self, s: str) -> List[str]:
        s = sorted(s)
        n = len(s)

        ans = []
        path = []
        vis = [False] * n  # 排列需要使用

        def dfs():
            if len(path) == n:
                ans.append("".join(path))

            for j in range(0, n):  # 每次从 0 开始选没用过的
                if vis[j]:
                    continue
                # 注意这个逻辑：去重复元素的影响
                if j > 0 and s[j] == s[j - 1] and not vis[j - 1]:
                    continue
                vis[j] = True
                path.append(s[j])
                dfs()
                path.pop()  # 恢复现场
                vis[j] = False
        dfs()
        return ans
