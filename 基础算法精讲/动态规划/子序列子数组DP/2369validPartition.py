# -*- coding: utf-8 -*-

"""
@File    : 2369validPartition.py
@Author  : wenhao
@Time    : 2023/4/19 22:14
@LC      : 2369
"""
from typing import List
from functools import cache


class Solution:
    # 记搜
    def validPartition(self, nums: List[int]) -> bool:
        @cache
        def dfs(i: int) -> bool:
            if i < 0: return True  # 无剩余
            if i == 0: return False  # 剩一个

            res = False
            # 情况 1
            if nums[i] == nums[i - 1]:
                res |= dfs(i - 2)
            if i >= 2:
                # 情况 2
                if nums[i] == nums[i - 1] and nums[i - 1] == nums[i - 2]:
                    res |= dfs(i - 3)
                # 情况 3
                if nums[i - 2] + 1 == nums[i - 1] and nums[i - 1] + 1 == nums[i]:
                    res |= dfs(i - 3)
            return res

        # 返回答案
        return dfs(len(nums) - 1)

    # 递推
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        f = [False] * (n + 1)
        f[0] = True  # 对应 -1 位置
        f[1] = False  # 对应 0 位置

        for i in range(2, n + 1):  # 这个 i 对应 f 不是 nums
            res = False
            # 情况 1
            if nums[i - 1] == nums[i - 2]:
                res |= f[i - 2]
            if i >= 3:
                # 情况 2
                if nums[i - 1] == nums[i - 2] and nums[i - 2] == nums[i - 3]:
                    res |= f[i - 3]
                # 情况 3
                if nums[i - 3] + 1 == nums[i - 2] and nums[i - 2] + 1 == nums[i - 1]:
                    res |= f[i - 3]
            f[i] |= res

        return f[-1]
