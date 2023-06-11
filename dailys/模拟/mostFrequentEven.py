# -*- coding: utf-8 -*-

"""
@File    : mostFrequentEven.py
@Author  : wenhao
@Time    : 2023/4/13 8:46
@LC      : 2404
"""
from typing import List
from collections import Counter


class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        nums.sort()
        cnt = Counter()

        ans = -1
        for num in nums:
            if (num & 1) == 0:
                cnt[num] += 1
                if cnt[num] > cnt[ans]:
                    ans = num
        return ans








