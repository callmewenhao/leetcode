# -*- coding: utf-8 -*-

"""
@File    : movesToMakeZigzag.py
@Author  : wenhao
@Time    : 2023/2/27 8:58
@LC      : 1144
"""
from typing import List
import math

class Solution:
    # 灵神
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        s = [0] * 2
        for i, x in enumerate(nums):
            left = nums[i - 1] if i else math.inf
            right = nums[i + 1] if i < len(nums) - 1 else math.inf
            s[i % 2] += max(x - min(left, right) + 1, 0)
        return min(s)

    def movesToMakeZigzag1(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:  # 特判 😢
            return 0

        c1, c2 = 0, 0
        for i, num in enumerate(nums):
            if (i & 1) == 0:  # 是个偶数 😊
                # 偶数减
                if i == 0 and num >= nums[i + 1]:
                    c1 += (num - nums[i + 1] + 1)
                elif i == n - 1 and num >= nums[i - 1]:
                    c1 += (num - nums[i - 1] + 1)
                elif 0 < i < n - 1:
                    mi = min(nums[i - 1], nums[i + 1])
                    if num >= mi:
                        c1 += (num - mi + 1)
            else:  # 是个奇数
                # 奇数减
                if i == n - 1 and num >= nums[i - 1]:
                    c2 += (num - nums[i - 1] + 1)
                elif 0 < i < n - 1:
                    mi = min(nums[i - 1], nums[i + 1])
                    if num >= mi:
                        c2 += (num - mi + 1)

        return min(c1, c2)
