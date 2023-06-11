# -*- coding: utf-8 -*-

"""
@File    : lastSubstring.py
@Author  : wenhao
@Time    : 2023/4/24 9:23
@LC      : 1163
"""


class Solution:
    # 抄的
    def lastSubstring(self, s: str) -> str:
        i, j, n = 0, 1, len(s)
        while j < n:
            k = 0
            while j + k < n and s[i + k] == s[j + k]:
                k += 1
            if j + k < n and s[i + k] < s[j + k]:
                i, j = j, max(j + 1, i + k + 1)
            else:
                j = j + k + 1
        return s[i:]