# -*- coding: utf-8 -*-

"""
@File    : 15threeSum.py
@Author  : wenhao
@Time    : 2023/5/30 22:59
@LC      : 15
"""
from typing import Optional, List
from collections import Counter

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        ans = set()
        n = len(nums)
        for i in range(n - 2):
            target = -nums[i]
            cnt = set()
            for j in range(i + 1, n):
                if target - nums[j] in cnt:
                    ans.add((nums[i], target - nums[j], nums[j]))
                else:
                    cnt.add(nums[j])

        ans = [[x, y, z] for x, y, z in ans]
        return ans

