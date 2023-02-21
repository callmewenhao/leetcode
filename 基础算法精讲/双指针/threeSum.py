# -*- coding: utf-8 -*-

"""
@File    : threeSum.py
@Author  : wenhao
@Time    : 2023/1/29 21:55
"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        nums.sort()

        for l in range(n - 2):
            if 0 < l and nums[l] == nums[l - 1]:
                continue
            # 提前结束
            if nums[l] > 0:
                break
            if nums[l] + nums[-2] + nums[-1] < 0:
                continue
            m, r = l + 1, n - 1
            while m < r:
                s = nums[m] + nums[r]
                if s < -nums[l]:
                    m += 1
                elif s > -nums[l]:
                    r -= 1
                else:
                    ans.append([nums[l], nums[m], nums[r]])
                    m += 1
                    while m < r and nums[m] == nums[m - 1]:
                        m += 1
                    r -= 1
                    while m < r and nums[r] == nums[r + 1]:
                        r -= 1

        return ans
