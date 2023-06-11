# -*- coding: utf-8 -*-

"""
@File    : T4.py
@Author  : wenhao
@Time    : 2023/6/4 11:42
@LC      : 
"""
from typing import List
from math import inf
from functools import cache
from itertools import accumulate
from collections import Counter


class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:

        @cache
        def f(s: str, i: int, pre_sum: int, limit: int, lead: int) -> int:
            if i == len(s):
                if min_sum <= pre_sum <= max_sum:
                    return 1
                return 0


            res = 0
            # 判断是否可以不选
            if not lead:  # 选择跳过
                res += f(s, i + 1,pre_sum, False, False)
            # 选数
            low = 1 - int(lead)
            up = int(s[i]) if limit else 9
            for x in range(low, up + 1):
                res += f(s, i + 1, pre_sum + x, limit and x == up, True)
            return res

        return (f(num2, 0, 0, True, False) - f(str(int(num1) - 1), 0, 0, True, False)) % (10**9+7)
