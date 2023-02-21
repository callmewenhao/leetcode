# -*- coding: utf-8 -*-

"""
@File    : lengthOfLongestSubstring.py
@Author  : wenhao
@Time    : 2023/1/29 21:22
"""
"""
滑窗
"""
from collections import Counter


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = l = 0
        c = Counter()
        for r, ch in enumerate(s):
            c[ch] += 1
            while c[ch] > 1:
                c[s[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)

        return ans
