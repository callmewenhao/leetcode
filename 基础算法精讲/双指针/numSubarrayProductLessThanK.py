# -*- coding: utf-8 -*-

"""
@File    : numSubarrayProductLessThanK.py
@Author  : wenhao
@Time    : 2023/1/29 21:09
"""
"""
滑窗
"""
from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        ans = 0
        left = 0
        prod = 1
        for right, val in enumerate(nums):
            prod *= val
            while left <= right and prod >= k:
                prod /= nums[left]
                left += 1
            ans += right - left + 1

        return ans
