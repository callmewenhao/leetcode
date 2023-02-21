# -*- coding: utf-8 -*-

"""
@File    : numberOfPairs.py
@Author  : wenhao
@Time    : 2023/2/16 16:02
@LC      : 2341
"""
from typing import List


class Solution:
    # 时间复杂度：O(n)
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        t = [0] * 101
        ans = [0, 0]
        for num in nums:
            t[num] += 1
            if t[num] % 2 == 0:
                ans[0] += 1
        ans[1] = len(nums) - 2 * ans[0]
        return ans


    # 时间复杂度：O(n * logn)
    def numberOfPairs1(self, nums: List[int]) -> List[int]:
        nums.sort()

        ans = [0, 0]
        val, cnt = -1, 1
        for i, num in enumerate(nums):
            if num == val:
                cnt += 1

            else:
                cnt = 1
                val = num

            if cnt % 2 == 0:  # 成对的删去相同的数字
                ans[0] += 1

        ans[1] = len(nums) - 2 * ans[0]
        return ans
