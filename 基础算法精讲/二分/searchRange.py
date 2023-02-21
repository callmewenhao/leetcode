# -*- coding: utf-8 -*-

"""
@File    : searchRange.py
@Author  : wenhao
@Time    : 2023/1/30 15:11
"""
from typing import List

"""
return the val larger than (or equal to) target
大于 lower_bound(nums, target + 1)
小于 lower_bound(nums, target) - 1
小于等于 lower_bound(nums, target + 1) - 1
都可以通过这个函数变换得到
"""


def lower_bound(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums) - 1  # [left, right]
    while left <= right:  # [left, right]
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        if nums[mid] >= target:
            right = mid - 1
    return left


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = lower_bound(nums, target)
        if start == len(nums) or nums[start] != target:
            return [-1, -1]
        end = lower_bound(nums, target + 1) - 1
        return [start, end]
