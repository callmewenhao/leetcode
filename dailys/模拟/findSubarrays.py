# -*- coding: utf-8 -*-

"""
@File    : findSubarrays.py
@Author  : wenhao
@Time    : 2023/3/26 8:52
@LC      : 2395
"""
from typing import List
from itertools import pairwise
from collections import Counter


class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        cnt = Counter()
        for x, y in pairwise(nums):
            s = x + y
            if s in cnt:
                return True
            cnt[s] += 1
        return False


