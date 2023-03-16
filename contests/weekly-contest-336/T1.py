# -*- coding: utf-8 -*-

"""
@File    : T1.py
@Author  : wenhao
@Time    : 2023/3/12 10:03
@LC      : 
"""
from typing import List
from collections import Counter
from itertools import accumulate


class Solution:
    # python 一行 统计 bool 值
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        return sum(w[0] in "aeiou" and w[-1] in "aeiou" for w in words)

    # 简单模拟题 😁
    def vowelStrings1(self, words: List[str], left: int, right: int) -> int:
        d = "aeiou"
        ans = 0
        for i in range(left, right + 1):
            if words[i][0] in d and words[i][-1] in d:
                ans += 1
        return ans
