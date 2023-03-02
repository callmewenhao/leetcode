# -*- coding: utf-8 -*-

"""
@File    : mergeSimilarItems.py
@Author  : wenhao
@Time    : 2023/2/28 8:26
@LC      : 2363
"""
from typing import List
from collections import Counter

class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        c = Counter()
        for k, v in items1:
            c[k] += v
        for k, v in items2:
            c[k] += v
        ans = list(c.items())
        ans.sort()
        return ans
