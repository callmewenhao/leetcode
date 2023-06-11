# -*- coding: utf-8 -*-

"""
@File    : T1.py
@Author  : wenhao
@Time    : 2023/4/16 10:07
@LC      : 
"""
from typing import List
from collections import Counter


class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        n = len(mat)
        cnt = [0] * n

        for i in range(n):
            cnt[i] = sum(mat[i])

        ans = [0, 0]
        for i in range(n):
            if ans[1] < cnt[i]:
                ans = [i, cnt[i]]
        return ans
