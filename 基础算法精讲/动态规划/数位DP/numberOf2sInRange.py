# -*- coding: utf-8 -*-

"""
@File    : numberOf2sInRange.py
@Author  : wenhao
@Time    : 2023/3/21 9:57
@LC      : 17.06
"""
from functools import cache


class Solution:
    # 数位 dp 典中典
    def numberOf2sInRange(self, n: int) -> int:
        s = str(n)
        @cache
        def f(i: int, cnt: int, limit: int) -> int:
            if i == len(s):
                return cnt
            res = 0
            low = 0
            up = int(s[i]) if limit else 9
            for d in range(low, up + 1):
                if d == 2:
                    res += f(i + 1, cnt + 1, limit and d == up)
                else:
                    res += f(i + 1, cnt, limit and d == up)
            return res
        return f(0, 0, True)
