# -*- coding: utf-8 -*-

"""
@File    : findSubstringInWraproundString.py
@Author  : wenhao
@Time    : 2023/3/12 22:24
@LC      : 467
"""
from typing import List
from collections import defaultdict


class Solution:
    # 看的答案😊
    def findSubstringInWraproundString(self, s: str) -> int:
        d = defaultdict(int)

        k = 0
        for i, ch in enumerate(s):
            if i > 0 and (ord(ch) - ord(s[i - 1])) % 26 == 1:
                k += 1
            else:
                k = 1
            d[ch] = max(k, d[ch])
        return sum(d.values())
