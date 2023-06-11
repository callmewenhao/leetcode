# -*- coding: utf-8 -*-

"""
@File    : countSubstrings.py
@Author  : wenhao
@Time    : 2023/3/27 10:50
@LC      : 1638
"""


class Solution:
    # 不得不说 灵神思路是很牛的 👏
    def countSubstrings(self, s: str, t: str) -> int:
        ans, n, m = 0, len(s), len(t)
        for d in range(1 - m, n):  # 枚举差值 s 比 t 多出来的长度
            i = max(d, 0)
            k0 = k1 = i - 1
            while i < n and i - d < m:  # i < n and j < m
                if s[i] != t[i - d]:
                    k0 = k1
                    k1 = i
                ans += k1 - k0
                i += 1
        return ans
