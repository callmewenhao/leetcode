# -*- coding: utf-8 -*-

"""
@File    : digitsCount.py
@Author  : wenhao
@Time    : 2023/3/20 22:37
@LC      : 1067
"""
from functools import cache


class Solution:
    # 简直和 那道题一样😁
    # 待优化👏
    def digitsCount(self, d: int, low: int, high: int) -> int:
        @cache
        def f(s: str, i: int, cnt: int, limit: int, lead: int) -> int:
            if i == len(s):
                return cnt
            res = 0
            # 判断是否可以不选
            if not lead:  # 选择跳过
                res += f(s, i + 1, cnt, False, False)
            # 选数
            low = 1 - int(lead)
            up = int(s[i]) if limit else 9
            for x in range(low, up + 1):
                if x == d:
                    res += f(s, i + 1, cnt + 1, limit and x == up, True)
                else:
                    res += f(s, i + 1, cnt, limit and x == up, True)
            return res

        return f(str(high), 0, 0, True, False) - f(str(low - 1), 0, 0, True, False)
