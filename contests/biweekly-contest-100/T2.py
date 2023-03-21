# -*- coding: utf-8 -*-

"""
@File    : T2.py
@Author  : wenhao
@Time    : 2023/3/18 22:12
@LC      : 
"""
from typing import List
from collections import Counter


class Solution:
    # 排序 + 双指针 😁
    # 优化 用大的值匹配小的值 而不是为小值匹配大值
    def maximizeGreatness(self, nums: List[int]) -> int:
        nums.sort()  # 小 -> 大 排序
        i = 0  # 维护待匹配的小值
        for x in nums:
            if x > nums[i]:  # 遍历到的元素 > 待匹配的小值
                i += 1
        return i

    # 利用两个指针的距离 👏 降维打击
    # 考虑无法匹配的个数 m 答案为 nums 的长度减去 m
    def maximizeGreatness1(self, nums: List[int]) -> int:
        return len(nums) - max(Counter(nums).values())

    def maximizeGreatness2(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        ans = 0
        i, j = 0, 1
        while j < n:
            while j < n and nums[i] >= nums[j]:
                j += 1
            if j < n:
                ans += 1
            i += 1
            j += 1
        return ans
