# -*- coding: utf-8 -*-

"""
@File    : rob.py
@Author  : wenhao
@Time    : 2023/2/10 10:13
@LC      : 198
"""
from typing import List
from functools import cache


class Solution:

    # 记忆化搜索和dp可以把时间复杂度优化到o(n)🤗
    # 状态压缩==滚动数组优化😊
    def rob(self, nums: List[int]) -> int:
        f0 = f1 = 0
        for num in nums:
            f0, f1 = f1, max(f1, f0 + num)
        return f1

    # dp 写法
    def rob3(self, nums: List[int]) -> int:
        n = len(nums)
        f = [0] * (n + 2)
        for i, num in enumerate(nums, 2):
            f[i] = max(f[i - 1], f[i - 2] + num)
        return f[-1]

    # 记忆化搜索👏
    def rob2(self, nums: List[int]) -> int:
        # @cache  # 使用hashmap存储入参以及对应返回值，其他语言用数组存储即可
        # def dfs(i: int) -> int:
        #     if i < 0:
        #         return 0
        #     return max(dfs(i - 1), dfs(i - 2) + nums[i])
        # return dfs(len(nums) - 1)
        n = len(nums)
        cache = [-1] * n # 数组存储
        def dfs(i: int) -> int:
            if i < 0:
                return 0
            if cache[i] != -1:
                return cache[i]
            cache[i] = max(dfs(i - 1), dfs(i - 2) + nums[i])
            return cache[i]
        return dfs(len(nums) - 1)

    # 回溯写法：时间复杂度是指数级别👈，lc 提示 TLE
    def rob1(self, nums: List[int]) -> int:
        def dfs(i: int) -> int:
            if i < 0:
                return 0
            return max(dfs(i - 1), dfs(i - 2) + nums[i])

        return dfs(len(nums) - 1)
