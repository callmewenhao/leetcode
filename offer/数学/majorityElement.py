# -*- coding: utf-8 -*-

"""
@File    : majorityElement.py
@Author  : wenhao
@Time    : 2023/2/9 10:33
@LC      : 169
"""
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        x = nums[0]
        votes = 1
        for i in range(1, len(nums)):
            if votes == 0:
                x = nums[i]
            votes += 1 if x == nums[i] else -1
        return x










