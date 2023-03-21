# -*- coding: utf-8 -*-

"""
@File    : findIntegers.py
@Author  : wenhao
@Time    : 2023/3/20 21:47
@LC      : 600
"""
from functools import cache


class Solution:
    # 30 位的二进制数 待优化 😂
    def findIntegers(self, n: int) -> int:
        s = f"{n:b}"

        @cache
        def f(i: int, last: int, limit: int) -> int:
            if i == len(s):
                return 1
            res = 0
            up = int(s[i]) if limit else 1
            for d in range(up + 1):
                if d == 1 and last == 1:
                    continue
                res += f(i + 1, d, limit and d == up)
            return res

        return f(0, 0, True)
