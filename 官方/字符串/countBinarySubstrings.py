# -*- coding: utf-8 -*-

"""
@File    : countBinarySubstrings.py
@Author  : wenhao
@Time    : 2023/3/12 22:04
@LC      : 696
"""
from itertools import accumulate, pairwise
from collections import Counter

class Solution:
    # 我是 sb 😤
    def countBinarySubstrings(self, s: str) -> int:
        fragments = []

        frag = ""
        for ch in s:
            if frag:
                if frag[0] != ch:
                    fragments.append(len(frag))
                    frag = ch
                else:
                    frag += ch
            else:
                frag += ch
        fragments.append(len(frag))

        # print(fragments)

        ans = 0
        for f, b in pairwise(fragments):
            ans += min(f, b)
        return ans
