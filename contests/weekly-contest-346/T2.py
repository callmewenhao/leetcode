# -*- coding: utf-8 -*-

"""
@File    : T2.py
@Author  : wenhao
@Time    : 2023/5/21 10:09
@LC      : 
"""
from typing import List
from math import inf
from functools import cache
from itertools import accumulate
from collections import Counter


class Solution:
    # 贪心😁
    # 字符串没法改 所以要转成列表
    def makeSmallestPalindrome(self, s: str) -> str:
        s = list(s)
        n = len(s)
        for i in range(n // 2):
            x, y = s[i], s[n - 1 - i]
            if  x < y:
                s[n - 1 - i] = x
            else:
                s[i] = y
        return ''.join(s)
