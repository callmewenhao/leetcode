# -*- coding: utf-8 -*-

"""
@File    : search.py
@Author  : wenhao
@Time    : 2023/1/30 16:21
@LC      : 33
"""
from typing import List


class Solution:
    # official
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:  # 返回答案
                return mid
            if nums[mid] > nums[-1]:  # 在左半部分
                if nums[-1] < target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            if nums[mid] <= nums[-1]:  # 在右半部分
                if target < nums[mid] or target > nums[-1]:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1  # 没找到

    def search1(self, nums: List[int], target: int) -> int:
        def in_left(i: int) -> bool:
            end = nums[-1]
            if nums[i] > end:
                return end < target <= nums[i]
            else:
                return target <= nums[i] or target > end

        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if in_left(mid):
                right = mid - 1
            else:
                left = mid + 1
        if left == len(nums) or nums[left] != target:
            return -1
        return left
