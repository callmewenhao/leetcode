# -*- coding: utf-8 -*-

"""
@File    : nthMagicalNumber.py
@Author  : wenhao
@Time    : 2023/2/10 14:54
@LC      : 878
"""
from math import lcm


class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        MOD = 10 ** 9 + 7
        a_b = lcm(a, b)

        def check(mx: int) -> bool:
            return mx // a + mx // b - mx // a_b >= n

        # 二分开区间版本
        l, r = 0, min(a, b) * n + 1
        while l + 1 < r:
            m = l + (r - l) // 2
            if check(m):
                r = m
            else:
                l = m
        return r % MOD

        # # 二分闭区间版本
        # l, r = 1, min(a, b) * n
        # while l <= r:
        #     m = l + (r - l) // 2
        #     if check(m):
        #         r = m - 1
        #     else:
        #         l = m + 1
        # return l % MOD
