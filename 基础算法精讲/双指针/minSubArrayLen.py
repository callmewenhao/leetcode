# -*- coding: utf-8 -*-

"""
@File    : minSubArrayLen.py
@Author  : wenhao
@Time    : 2023/1/29 20:27
"""
"""
滑窗
"""
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sum = 0
        ans = len(nums)
        i = 0
        for j, val in enumerate(nums):
            sum += val

            while sum >= target:
                ans = min(ans, j - i + 1)
                sum -= nums[i]
                i += 1

        return ans if ans != len(nums) else 0


