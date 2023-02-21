# -*- coding: utf-8 -*-

"""
@File    : subsets.py
@Author  : wenhao
@Time    : 2023/1/31 21:02
@LC      : 78
"""
from typing import List


class Solution:
    # 2
    def subsets1(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []
        n = len(nums)

        def dfs(i: int):
            ans.append(path.copy())
            if i == n:
                return
            for j in range(i, n):
                path.append(nums[j])
                dfs(j + 1)
                path.pop()

        dfs(0)
        return ans

    # 1
    def subsets1(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []
        n = len(nums)

        def dfs(i: int):
            if i == n:
                ans.append(path.copy())  # 注意深拷贝
                return
            # 不选
            dfs(i + 1)
            # 选
            path.append(nums[i])
            dfs(i + 1)
            path.pop()

        dfs(0)
        return ans
