# -*- coding: utf-8 -*-

"""
@File    : minimizeArrayValue.py
@Author  : wenhao
@Time    : 2023/2/9 21:03
@LC      : 2439
"""
import bisect
from typing import List


class Solution:
    # 这题灵神提供了一个分类讨论的解法👍
    # optimize
    '''
    优化check，减少空间复杂度
    '''
    def minimizeArrayValue(self, nums: List[int]) -> int:
        def check(mx: int) -> bool:
            extra = 0
            for i in range(len(nums) - 1, 0, -1):
                dif = nums[i] - mx
                extra = max(extra + dif, 0)
            return nums[0] + extra <= mx

        # l, r = nums[0], max(nums)
        # while l <= r:
        #     m = l + (r - l) // 2
        #     if check(m):
        #         r = m - 1
        #     else:
        #         l = m + 1
        # return l
        return bisect.bisect_left(range(max(nums)), True, key=check)

    def minimizeArrayValue1(self, nums: List[int]) -> int:
        def check(mx: int) -> bool:
            # if mx < nums[0]:
            #     return False
            buf = nums.copy()
            for i in range(len(buf) - 1, 0, -1):
                dif = buf[i] - mx
                if dif > 0:
                    buf[i - 1] += dif
            return buf[0] <= mx

        l, r = nums[0], max(nums)
        while l <= r:
            m = l + (r - l) // 2
            if check(m):
                r = m - 1
            else:
                l = m + 1
        return l
