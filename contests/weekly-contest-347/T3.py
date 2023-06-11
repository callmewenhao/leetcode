# -*- coding: utf-8 -*-

"""
@File    : T3.py
@Author  : wenhao
@Time    : 2023/5/28 10:24
@LC      : 
"""
from typing import List
from math import inf
from functools import cache
from itertools import accumulate
from collections import Counter


class Solution:


    def minimumCost(self, s: str) -> int:
        n = len(s)

        def f(ch: str) -> int:
            # 变成 ch
            res = 0
            carry = 0
            for i in range(n // 2 - 1, -1, -1):
                if s[i] == ch:
                    if carry % 2 == 0:
                        continue
                    else:
                        res += i + 1
                        carry += 1
                if s[i] != ch:
                    if carry % 2 == 1:
                        continue
                    else:
                        res += i + 1
                        carry += 1
            carry = 0
            for i in range(n // 2, n):
                if s[i] == ch:
                    if carry % 2 == 0:
                        continue
                    else:
                        res += n - i
                        carry += 1
                if s[i] != ch:
                    if carry % 2 == 1:
                        continue
                    else:
                        res += n - i
                        carry += 1
            return res

        return min(f('0'), f('1'))





