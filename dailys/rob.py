# -*- coding: utf-8 -*-

"""
@File    : rob.py
@Author  : wenhao
@Time    : 2023/2/9 9:05
@LC      : 198
"""
from typing import List
from functools import cache


class Solution:
    # 记忆化搜索
    def rob(self, nums: List[int]) -> int:
        @cache
        def dfs(i: int) -> int:
            if i == 0:  # 一间房
                return nums[i]
            if i == 1:  # 两间房
                return max(nums[i], nums[i - 1])
            # 其他情况
            return max(dfs(i - 1), dfs(i - 2) + nums[i])

        return dfs(len(nums) - 1)

    # dp
    def rob1(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n + 1)  # 多开一个单位的数组，应对两间房
        dp[1] = nums[0]  # 一间房初始化

        for i in range(2, n + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])

        return dp[-1]
