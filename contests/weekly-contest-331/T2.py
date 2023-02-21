# -*- coding: utf-8 -*-

"""
@File    : T2.py
@Author  : wenhao
@Time    : 2023/2/5 10:01
@LC      : 
"""
from typing import List
from collections import Counter


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        s = {'a', 'e', 'i', 'o', 'u'}
        nums = []
        for word in words:
            if word[0] in s and word[-1] in s:
                nums.append(1)
            else:
                nums.append(0)

        pre_sum = [0] * (len(nums) + 1)
        for i, num in enumerate(nums):
            pre_sum[i + 1] = pre_sum[i] + num

        ans = []
        for l, r in queries:
            ans.append(pre_sum[r] - pre_sum[l - 1])
        return ans
