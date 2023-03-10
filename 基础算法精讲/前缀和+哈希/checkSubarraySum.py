# -*- coding: utf-8 -*-

"""
@File    : checkSubarraySum.py
@Author  : wenhao
@Time    : 2023/3/10 15:04
@LC      : 523
"""
from typing import List
from collections import Counter

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        s = 0
        c = Counter({0: -1})  # 初始化

        n = len(nums)
        for i in range(n):
            s += nums[i]
            m = s % k
            if m in c:
                if i - c[m] >= 2:
                    return True
            else:
                c[m] = i  # 只存最小的
        return False
