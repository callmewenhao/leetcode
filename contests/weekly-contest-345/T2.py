# -*- coding: utf-8 -*-

"""
@File    : T2.py
@Author  : wenhao
@Time    : 2023/5/14 10:23
@LC      : 
"""
from typing import List
from math import inf
from functools import cache
from itertools import accumulate
from collections import Counter


class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        n = len(derived)
        c1 = [1]
        c2 = [0]
        for i in range(1, n):
            c1.append(derived[i - 1] ^ c1[-1])
            c2.append(derived[i - 1] ^ c2[-1])
        if c1[-1] ^ c1[0] == derived[0] or c2[-1] ^ c2[0] == derived[0]:
            return True
        return False



