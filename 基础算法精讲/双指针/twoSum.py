# -*- coding: utf-8 -*-

"""
@File    : twoSum.py
@Author  : wenhao
@Time    : 2023/1/29 21:34
"""
"""
相向双指针
"""

from typing import List


class Solution:
    # optimize
    def twoSum(self, nums: List[int], t: int) -> List[int]:
        n = len(nums)
        l, r = 0, n - 1
        while l < r:
            if nums[l] + nums[r] < t:
                l += 1
            elif nums[l] + nums[r] > t:
                r -= 1
            else:
                break
        return [l + 1, r + 1]

    def twoSum1(self, nums: List[int], t: int) -> List[int]:
        l, r = 0, len(nums) - 1
        while nums[l] + nums[r] != t:
            if nums[l] + nums[r] < t:
                l += 1
            else:
                r -= 1
        return [l, r]
