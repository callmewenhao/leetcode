# -*- coding: utf-8 -*-

"""
@File    : jump.py
@Author  : wenhao
@Time    : 2023/2/21 9:31
@LC      : 45
"""
from typing import List


class Solution:
    # 优化 贪心思想
    # 每次在上次能跳到的范围（end）内选择一个能跳的最远的位置
    # 也就是能跳到 max_far 位置的点 作为下次的起跳点
    class Solution:
        def jump(self, nums: List[int]) -> int:
            n = len(nums)
            ans = 0
            end = 0
            new_end = 0

            for i in range(n - 1):
                new_end = max(new_end, i + nums[i])
                if i == end:
                    ans += 1
                    end = new_end
            return ans









    def jump1(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        curRight = 0
        mostRight = nums[0]

        while curRight < n - 1:
            ans += 1
            if mostRight >= n - 1:
                break

            idx, newMostRight = curRight, mostRight
            for i in range(curRight, mostRight + 1):
                if newMostRight < i + nums[i]:
                    idx = i
                    newMostRight = i + nums[i]
            curRight = idx
            mostRight = newMostRight

        return ans












