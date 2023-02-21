# -*- coding: utf-8 -*-

"""
@File    : findKthLargest.py
@Author  : wenhao
@Time    : 2023/2/1 11:11
@LC      : 
"""
from typing import List
from sortedcontainers import SortedList


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        s = SortedList()

        for i in range(k):
            s.add(nums[i])

        for i in range(k, n):
            if nums[i] > s[0]:
                s.add(nums[i])
                s.pop(index=0)

        return s[0]
