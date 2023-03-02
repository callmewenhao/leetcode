# -*- coding: utf-8 -*-

"""
@File    : moveZeroes.py
@Author  : wenhao
@Time    : 2023/3/2 22:40
@LC      : 283
"""
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 双指针 快慢指针
        # 快指针遍历一边元素
        # 慢指针维护可覆盖的位置
        s = 0
        for i, num in enumerate(nums):
            if num != 0:
                nums[s] = num
                s += 1
        for i in range(s, len(nums)):
            nums[i] = 0
