# -*- coding: utf-8 -*-

"""
@File    : maxRotateFunction.py
@Author  : wenhao
@Time    : 2023/3/4 10:22
@LC      : 396
"""
from typing import List


class Solution:
    # 这个题目需要好好在纸上推算
    # 寻找前后结果的差值 f = f + n * nums[i] - s
    # 以 测试用例 1 为例
    # 4 2 3 6
    # n = 4  s = 15  f = 0 * 4 + 1 * 2 + 2 * 3 + 3 * 6
    # 0: f = f + n * nums[0] - s
    # 1: f = f + n * nums[1] - s
    # 2: f = f + n * nums[2] - s
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        s = sum(nums)
        f = sum(num * i for num, i in zip(nums, range(n)))

        ans = f
        for i in range(n - 1):
            f = f + n * nums[i] - s
            ans = max(ans, f)
        return ans
