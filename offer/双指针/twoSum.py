# -*- coding: utf-8 -*-

"""
@File    : twoSum.py
@Author  : wenhao
@Time    : 2023/1/30 10:28
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        l, r = 0, n - 1
        while l < r:
            s = nums[l] + nums[r]
            if s < target:
                l += 1
            elif s > target:
                r -= 1
            else:
                break
        return [nums[l], nums[r]]
