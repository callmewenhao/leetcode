# -*- coding: utf-8 -*-

"""
@File    : findMin.py
@Author  : wenhao
@Time    : 2023/1/30 16:08
@LC      : 153
"""
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 2
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > nums[-1]:
                left = mid + 1
            else: # nums[mid] 与 nums[0] 不会相等
                right = mid - 1
        return nums[left]

