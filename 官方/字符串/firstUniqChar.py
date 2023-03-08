# -*- coding: utf-8 -*-

"""
@File    : firstUniqChar.py
@Author  : wenhao
@Time    : 2023/3/7 10:56
@LC      : 387
"""
from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        c = Counter(s)
        for i, ch in enumerate(s):
            if c[ch] == 1:
                return i
        return -1



