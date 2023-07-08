# -*- coding: utf-8 -*-

"""
@File    : T3.py
@Author  : wenhao
@Time    : 2023/6/25 10:27
@LC      : 
"""

class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:

        last = -1
        ans = 0
        for i, num in enumerate(nums):
            if num == 1:
                if last == -1:
                    last = i
                else:
                    ans = (ans * (i - last)) % (10**9+7)
        return ans


