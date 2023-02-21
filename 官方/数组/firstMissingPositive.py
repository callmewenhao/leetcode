# -*- coding: utf-8 -*-

"""
@File    : firstMissingPositive.py
@Author  : wenhao
@Time    : 2023/2/16 10:48
@LC      : 41 原地 hash
"""
from typing import List


class Solution:
    # 另一种算法：位置交换——桶排序


    # 原地 hash，对在范围内 且遍历过的数 打上标记
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if not (0 < nums[i] <= n):
                nums[i] = n + 1

        for i, num in enumerate(nums):
            num = abs(num)
            if 0 < num <= n and nums[num - 1] > 0:
                nums[num - 1] *= -1

        # print(nums)
        ans = n + 1
        for i in range(n):
            if nums[i] > 0:
                ans = i + 1
                break
        return ans
