# -*- coding: utf-8 -*-

"""
@File    : T3.py
@Author  : wenhao
@Time    : 2023/7/2 10:21
@LC      : 
"""
from typing import List
from collections import deque


class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        dq_max = deque()
        dq_min = deque()

        ans = 0
        l = 0
        for r, x in enumerate(nums):
            while dq_max and nums[dq_max[-1]] <= x:
                dq_max.pop()
            dq_max.append(r)

            while dq_min and nums[dq_min[-1]] >= x:
                dq_min.pop()
            dq_min.append(r)

            while nums[dq_max[0]] - nums[dq_min[0]] > 2:
                l += 1
                while dq_max and dq_max[0] < l:
                    dq_max.popleft()
                while dq_min and dq_min[0] < l:
                    dq_min.popleft()

            ans += r - l + 1

        return ans
