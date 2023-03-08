# -*- coding: utf-8 -*-

"""
@File    : frequencySort.py
@Author  : wenhao
@Time    : 2023/3/7 22:03
@LC      : 451
"""
import string


class Solution:
    def frequencySort(self, s: str) -> str:
        t = [[0, i] for i in range(128)]
        for ch in s:
            t[ord(ch)][0] += 1
        t.sort(reverse=True)
        # 优化
        return ''.join(chr(i) * v for v, i in t)

