# -*- coding: utf-8 -*-

"""
@File    : nthUglyNumber.py
@Author  : wenhao
@Time    : 2023/2/10 21:32
@LC      : 1201
"""
import math


class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        a_b = math.lcm(a, b)
        a_c = math.lcm(a, c)
        b_c = math.lcm(b, c)
        a_b_c = math.lcm(a, b, c)

        def check(mx: int) -> bool:
            # 计算倍数地个数
            n1 = mx // a + mx // b + mx // c \
                 - mx // a_b - mx // a_c - mx // b_c \
                 + mx // a_b_c
            return n1 >= n

        l, r = 1, min(a, b, c) * n
        while l <= r:
            mid = l + (r - l) // 2
            if check(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l