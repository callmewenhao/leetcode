# -*- coding: utf-8 -*-

"""
@File    : lengthOfLIS.py
@Author  : wenhao
@Time    : 2023/3/8 22:40
@LC      : 300
"""
from typing import List
from functools import cache
from bisect import bisect_left


class Solution:
    # 灵神的思考题目：如果要求不严格递增？
    # bisect_left 改为 bisect_right
    # if nums[j] < nums[i]: 改为 if nums[j] <= nums[i]:

    # 二分查找 + 贪心
    # 优化 空间
    def lengthOfLIS3(self, nums: List[int]) -> int:
        ng = 0
        for x in nums:
            i = bisect_left(nums, x, 0, ng)
            nums[i] = x
            if i == ng:
                ng += 1
        return ng

    # 优化
    # 二分查找 + 贪心
    def lengthOfLIS2(self, nums: List[int]) -> int:
        g = []
        for num in nums:
            p = bisect_left(g, num)
            if p == len(g):
                g.append(num)
            else:
                g[p] = num
        return len(g)

    # dp 递推
    def lengthOfLIS1(self, nums: List[int]) -> int:
        n = len(nums)
        f = [0] * n
        for i in range(n):
            res = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    res = max(res, f[j])
            f[i] = res + 1
        return max(f)

    # 记忆化搜索
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        @cache
        def dfs(i: int) -> int:
            # 当 i=0 时 for 循环不会进行 直接返回 1 就相当于边界条件
            res = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    res = max(res, dfs(j))
            return res + 1

        return max(dfs(i) for i in range(n))
