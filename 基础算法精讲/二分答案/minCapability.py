# -*- coding: utf-8 -*-

"""
@File    : minCapability.py
@Author  : wenhao
@Time    : 2023/2/9 19:47
@LC      : 2560
"""
'''
1. 二分答案
最小的最大值
单调性
猜一个最大值 mx，根据单调性进行二分，判断能否偷至少k间房屋

2. LC 198 打家劫舍
198题通过dp求偷窃的最大值，
本题可以使用dp求能够偷窃的最多房屋数目
'''
from typing import List
from bisect import bisect_left


class Solution:

    # optimize 滚动数组
    def minCapability(self, nums: List[int], k: int) -> int:
        n = len(nums)

        def check(mx: int) -> int:
            f0, f1 = 0, 0
            for i, num in enumerate(nums):
                if num <= mx:
                    f0, f1 = f1, max(f0 + 1, f1)
                else:
                    f0 = f1
            return f1

        return bisect_left(range(max(nums)), k, key=check)

    # dp
    def minCapability1(self, nums: List[int], k: int) -> int:
        n = len(nums)

        def check(mx: int) -> int:
            dp = [0] * (n + 2)
            for i, num in enumerate(nums):
                dp[i + 2] = dp[i + 1]
                if num <= mx:
                    dp[i + 2] = max(dp[i + 2], dp[i] + 1)
            return dp[-1]

        return bisect_left(range(max(nums) + 1), k, key=check)
