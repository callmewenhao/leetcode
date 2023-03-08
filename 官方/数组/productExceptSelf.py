# -*- coding: utf-8 -*-

"""
@File    : productExceptSelf.py
@Author  : wenhao
@Time    : 2023/3/5 16:02
@LC      : 238
"""
from typing import List


class Solution:
    # 用 1 个变量维护 前缀乘积
    # 用 1 个数组维护 后缀乘积
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        s2 = [1] * n
        for i in range(n - 2, -1, -1):
            s2[i] *= nums[i + 1] * s2[i + 1]
        s1 = 1
        ans = [0] * n
        for i, num in enumerate(nums):
            ans[i] = s1 * s2[i]
            s1 *= num
        return ans
