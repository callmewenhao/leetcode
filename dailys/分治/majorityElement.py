# -*- coding: utf-8 -*-

"""
@File    : majorityElement.py
@Author  : wenhao
@Time    : 2023/3/21 13:54
@LC      : 169
"""
from typing import List


class Solution:
    # 有一个贪心的投票解法，很简单😂 On
    # 这里用分治解决 Onlogn
    # 整体思路
    # 数组分两半 [left, mid) [mid, right) 分别找到大于 n // 2 的元素
    # 然后
    def majorityElement(self, nums: List[int]) -> int:
        def mergeFind(nums: List[int], left: int, right: int) -> int:
            if left + 1 == right:
                return nums[left]
            mid = (left + right) // 2
            n1 = mergeFind(nums, left, mid)
            n2 = mergeFind(nums, mid, right)

            cnt1 = sum(num == n1 for num in nums[left:right])
            cnt2 = sum(num == n2 for num in nums[left:right])
            return n1 if cnt1 > cnt2 else n2  # 必定在这里返回 🤣

        return mergeFind(nums, 0, len(nums))
