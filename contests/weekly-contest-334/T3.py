# -*- coding: utf-8 -*-

"""
@File    : beautifulSubarrays.py
@Author  : wenhao
@Time    : 2023/2/26 9:46
@LC      : 
"""
from typing import List


class Solution:
    # 确实是 二分答案 但是具体思路没想清楚
    #
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()

        l, r = 0, n // 2
        while l <= r:
            mid = l + (r - l) // 2
            # 对应的 check 函数
            flag = True
            for i in range(mid):
                if nums[i] * 2 > nums[n - mid + i]:
                    flag = False

            if flag:
                l = mid + 1
            else:
                r = mid - 1

        return 2 * r
