# -*- coding: utf-8 -*-

"""
@File    : minimumOperationsToZero.py
@Author  : wenhao
@Time    : 2023/1/7 10:51
"""
from typing import List


class Solution:
    # 逆向思维+双指针
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        if target < 0: return -1

        ans = -1
        left = s = 0
        for right, x in enumerate(nums):
            s += x
            while s > target:
                s -= nums[left]
                left += 1
            if s == target:
                ans = max(ans, right - left + 1)

        return ans if ans < 0 else len(nums) - ans


    # 先求后缀，再枚举前缀
    def minOperations1(self, nums: List[int], x: int) -> int:
        s, n = 0, len(nums)
        i, j = 0, n - 1
        while 0 <= j:
            if s + nums[j] > x:
                break
            s += nums[j]
            j -= 1
        if j == -1 and s < x: return -1

        ans = n + 1
        while i < n:
            if s == x:
                ans = min(ans, i + (n - j - 1))
                s += nums[i]
                i += 1
            elif s < x:
                s += nums[i]
                i += 1
            else:
                while s > x and j < n - 1:
                    j += 1
                    s -= nums[j]
                if s > x: break

        return ans if ans <= n else -1
