# -*- coding: utf-8 -*-

"""
@File    : rearrangeCharacters.py
@Author  : wenhao
@Time    : 2023/1/13 20:50
"""
from collections import Counter


class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        ans = 11
        cnt1 = Counter(s)
        cnt2 = Counter(target)
        for ch in cnt2:
            ans = min(ans, cnt1[ch] // cnt2[ch])
        return ans

