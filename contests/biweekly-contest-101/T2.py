# -*- coding: utf-8 -*-

"""
@File    : T2.py
@Author  : wenhao
@Time    : 2023/4/1 22:21
@LC      : 
"""
from typing import List
from collections import Counter


class Solution:
    # 常数空间优化
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        d = dict(zip(chars, vals))
        f = ans = 0  # 空串保底 0

        for ch in s:
            v = d.get(ch, ord(ch) - ord('a') + 1)
            f = max(v, f + v)
            ans = max(ans, f)
        return ans

    # 优化
    def maximumCostSubstring1(self, s: str, chars: str, vals: List[int]) -> int:
        d = dict(zip(chars, vals))
        n = len(s)
        f = [0] * (n + 1)
        for i, ch in enumerate(s):
            v = d.get(ch, ord(ch) - ord('a') + 1)
            f[i+1] = max(v, f[i] + v)
        return max(max(f), 0)

    def maximumCostSubstring1(self, s: str, chars: str, vals: List[int]) -> int:
        d = dict(zip(chars, vals))

        n = len(s)
        f = [0] * n
        f[0] = ord(s[0]) - ord('a') + 1 if s[0] not in d else d[s[0]]

        for i in range(1, n):
            v = ord(s[i]) - ord('a') + 1 if s[i] not in d else d[s[i]]
            f[i] = max(v, f[i - 1] + v)
        return max(0, max(f))
