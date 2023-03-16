# -*- coding: utf-8 -*-

"""
@File    : optimalDivision.py
@Author  : wenhao
@Time    : 2023/3/13 14:22
@LC      : 553
"""
from typing import List


class Solution:
    # 对于给定的输入只有一种最优除法
    # 没意思的一题 😒
    # 被除数始终是 nums[0] 则结果最大表示 除数尽可能小
    # 即剩余元素按顺序运算 num[0] / (nums[1]/.../nums[-1])
    def optimalDivision(self, nums: List[int]) -> str:
        ans = f"{nums[0]}"
        n = len(nums)
        if n == 1:
            return ans
        ans += '/'
        if n > 2:
            ans += "("
        for i in range(1, n):
            ans += str(nums[i])
            if i < n - 1:
                ans += '/'
        if n > 2:
            ans += ')'
        return ans
