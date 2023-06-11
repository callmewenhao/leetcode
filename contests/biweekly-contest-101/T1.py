# -*- coding: utf-8 -*-

"""
@File    : T1.py
@Author  : wenhao
@Time    : 2023/4/1 22:21
@LC      : 
"""
from typing import List
from collections import Counter


class Solution:
    # 位运算优化 👍 用 C++ 写了

    # hash 做法
    def minNumber1(self, nums1: List[int], nums2: List[int]) -> int:
        s1 = set(nums1)
        s2 = set(nums2)
        s = s1 & s2
        if s: return min(s)

        mi1 = min(nums1)
        mi2 = min(nums2)

        return min(mi1 * 10 + mi2, mi2 * 10 + mi1)

    def minNumber1(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()

        for n1 in nums1:
            if n1 in nums2:
                return n1

        mi1 = min(nums1)
        mi2 = min(nums2)

        return mi1 * 10 + mi2 if mi1 < mi2 else mi2 * 10 + mi1
