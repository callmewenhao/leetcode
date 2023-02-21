# -*- coding: utf-8 -*-

"""
@File    : T1.py
@Author  : wenhao
@Time    : 2023/2/19 10:05
@LC      : 
"""
from typing import List
from collections import Counter


class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        c = Counter()
        for id, val in nums1:
            c[id] += val
        for id, val in nums2:
            c[id] += val

        ans = []
        for k, v in c.items():
            ans.append([k, v])
        ans.sort(key=lambda x: x[0])
        return ans



