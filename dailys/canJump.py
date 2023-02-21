# -*- coding: utf-8 -*-

"""
@File    : canJump.py
@Author  : wenhao
@Time    : 2023/2/21 9:04
@LC      : 55
"""
from typing import List


class Solution:
    # 官方答案 贪心思想
    def canJump(self, nums: List[int]) -> bool:
        n, rightmost = len(nums), 0
        for i in range(n):
            if i <= rightmost:
                rightmost = max(rightmost, i + nums[i])
                if rightmost >= n - 1:
                    return True
        return False



    # 我的做法
    def canJump1(self, nums: List[int]) -> bool:
        cur_r = 0
        next_r = nums[0]
        n = len(nums)

        while cur_r < n - 1 and cur_r < next_r:
            cur_r += 1
            next_r = max(next_r, cur_r + nums[cur_r])
            if next_r >= n - 1:
                break

        return next_r >= n - 1


