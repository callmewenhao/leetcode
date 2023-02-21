# -*- coding: utf-8 -*-

"""
@File    : combinationSum2.py
@Author  : wenhao
@Time    : 2023/2/19 22:29
@LC      : 40
"""
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        ans = []
        path = []
        candidates.sort()

        # for 的写法
        def dfs(i: int, t):
            # 判断是否找到答案
            if t == 0:
                ans.append(path.copy())
                return
            # 剪枝
            if t < 0 or i >= n:
                return
            # 从 i 开始选，而不是选 i
            for j in range(i, n):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                path.append(candidates[j])  # 有 add
                dfs(j + 1, t - candidates[j])
                path.pop()  # 就得有 pop

        dfs(0, target)  # 从 0 开始选
        return ans



