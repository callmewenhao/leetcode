# -*- coding: utf-8 -*-

"""
@File    : findMaxConsecutiveOnes.py
@Author  : wenhao
@Time    : 2023/2/4 17:29
@LC      : 485
"""
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        cnt = 0
        for num in nums:
            if num == 0:
                ans = max(ans, cnt)
                cnt = 0
            else:
                cnt += 1
        ans = max(ans, cnt)
        return ans




