# -*- coding: utf-8 -*-

"""
@File    : commonFactors.py
@Author  : wenhao
@Time    : 2023/4/5 22:21
@LC      : 2427
"""
from math import gcd


class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        ans = 0
        t = gcd(a, b)  # 优化使用 gcd
        for num in range(1, t + 1):
            if t % num == 0:
                ans += 1
        return ans
