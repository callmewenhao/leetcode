# -*- coding: utf-8 -*-

"""
@File    : findPeakElement.py
@Author  : wenhao
@Time    : 2023/1/30 15:25
@LC      : 162
"""
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # 这里是闭区间写法
        left = 0
        right = len(nums) - 2  # 注意右侧边界需要从 len(nums) - 2 开始，否则数组越界
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid - 1
        return left
