# -*- coding: utf-8 -*-

"""
@File    : canPartition.py
@Author  : wenhao
@Time    : 2023/2/21 14:44
@LC      : 416
"""
from typing import List


class Solution:
    '''
    给你一个只包含正整数的非空数组 nums
    请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
    01背包🤗
    '''
    # 优化
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s & 1 > 0:
            return False

        n, t = len(nums), s // 2
        f = [False] * (t + 1)
        f[0] = True  # [0][0] 一定可以成功

        for i in range(n):
            for j in range(t, nums[i] - 1, -1):
                f[j] = f[j] or f[j - nums[i]]
        return f[t]

    def canPartition1(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s & 1 > 0:
            return False

        n, t = len(nums), s // 2
        f = [[False] * (t + 1) for _ in range(n + 1)]
        f[0][0] = True  # [0][0] 一定可以成功

        for i in range(n):
            for j in range(t + 1):
                if nums[i] > j:  # 当数值大于目标值时 只能用前面的数字
                    f[i + 1][j] = f[i][j]
                else:  # 否则有两种方式可能成功
                    f[i + 1][j] = f[i][j] or f[i][j - nums[i]]
        return f[n][t]










