# -*- coding: utf-8 -*-

"""
@File    : T2.py
@Author  : wenhao
@Time    : 2023/3/12 10:03
@LC      : 
"""
from typing import List
from collections import Counter
from itertools import accumulate


class Solution:
    # python 一行代码 😁
    def maxScore(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        # 还是对 bool 值求和 👍
        return sum(s > 0 for s in accumulate(nums))

    # 贪心思想 正数在前 负数在后 绝对值小的负数在前
    def maxScore1(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        pre = accumulate(nums)
        ans = 0
        for num in pre:
            if num > 0:
                ans += 1

        return ans
