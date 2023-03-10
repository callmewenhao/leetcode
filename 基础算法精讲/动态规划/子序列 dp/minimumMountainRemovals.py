# -*- coding: utf-8 -*-

"""
@File    : minimumMountainRemovals.py
@Author  : wenhao
@Time    : 2023/3/9 16:46
@LC      : 1671
"""
from typing import List


class Solution:
    # 思路就是找出每个位置 i 的前后递增最大子序列
    # 删除的元素个数就是 n - pre[i] - suf[i] - 1
    # 寻找每个位置 i 的前后递增最大子序列 可以使用 dp 或者 二分+贪心实现 类似 300 题😁
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        # 预处理
        n = len(nums)
        # 第 i 个元素前的递增子序列长度
        pre = [0] * n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i] and pre[j] + 1 > pre[i]:
                    pre[i] = pre[j] + 1
        # 第 i 个元素后的递增子序列长度
        suf = [0] * n
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if nums[j] < nums[i] and suf[j] + 1 > suf[i]:
                    suf[i] = suf[j] + 1
        ans = n
        for i in range(1, n - 1):
            if pre[i] and suf[i] and n - pre[i] - suf[i] - 1 < ans:
                ans = n - pre[i] - suf[i] - 1
        return ans
