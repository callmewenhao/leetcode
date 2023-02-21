# -*- coding: utf-8 -*-

"""
@File    : permute.py
@Author  : wenhao
@Time    : 2023/1/31 23:39
@LC      : 46 无重复全排列
"""
from typing import List


class Solution:
    # 更一般的写法
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        path = [0] * n
        on_path = [False] * n

        def dfs(i: int):
            if i == n:
                ans.append(path.copy())
                return
            for j in range(n):  # 枚举选哪个
                if not on_path[j]:
                    on_path[j] = True
                    path[i] = nums[j]
                    dfs(i + 1)
                    on_path[j] = False
        dfs(0)
        return ans

    # 这里使用 set
    def permute1(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        path = [0] * n

        def dfs(i: int, s):
            if i == n:
                ans.append(path.copy())
                return
            for num in s:  # 枚举选哪个
                path[i] = num
                dfs(i + 1, s - {num})

        dfs(0, set(nums))
        return ans
