# -*- coding: utf-8 -*-

"""
@File    : T1.py
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
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        vis = set()

        p = 0
        i = 1
        while p not in vis:
            vis.add(p)
            p = (p + i * k) % n
            i += 1

        ans= []
        for i in range(0, n):
            if i not in vis:
                ans.append(i+1)
        return sorted(ans)
