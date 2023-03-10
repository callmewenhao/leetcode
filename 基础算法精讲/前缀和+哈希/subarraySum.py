# -*- coding: utf-8 -*-

"""
@File    : subarraySum.py
@Author  : wenhao
@Time    : 2023/3/10 14:55
@LC      : 560
"""
from typing import List
from collections import Counter


class Solution:
    # 之所以不用滑窗是因为数组元素含有负值
    # 前缀和+hash 就可以避免这个问题
    def subarraySum(self, nums: List[int], k: int) -> int:
        s = 0
        c = Counter({0: 1})  # 初始化 0:1

        ans = 0  # 构造答案
        for num in nums:
            s += num
            if (s - k) in c:
                ans += c[s - k]
            c[s] += 1
        return ans
