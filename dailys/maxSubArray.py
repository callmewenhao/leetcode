# -*- coding: utf-8 -*-

"""
@File    : maxSubArray.py
@Author  : wenhao
@Time    : 2023/2/27 19:10
@LC      : 53
"""
from typing import List


class Solution:
    # 经典动态规划 i am an idiot 😣
    # 定义 f[i] 为以 nums[i] 结尾的最大和子数组 答案是 max(f)
    # 无非 2 种情况的最大值
    # f[i - 1] + nums[i] or nums[i]
    def maxSubArray(self, nums: List[int]) -> int:
        ans, n = nums[0], len(nums)  # 再递推的过程中 维护最大值（答案）
        f = [nums[0]] * n  # 注意边界应该是 nums[0]
        for i in range(1, n):
            f[i] = max(f[i - 1] + nums[i], nums[i])  # 状态方程
            ans = max(ans, f[i])  # 维护答案
        return ans












