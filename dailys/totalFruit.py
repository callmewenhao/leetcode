# -*- coding: utf-8 -*-

"""
@File    : totalFruit.py
@Author  : wenhao
@Time    : 2023/2/19 21:24
@LC      : 904
"""
from typing import List
from collections import Counter


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        c = Counter()
        l = ans = 0
        for r in range(n):
            c[fruits[r]] += 1

            while len(c) > 2:
                c[fruits[l]] -= 1
                if c[fruits[l]] == 0:
                    c.pop(fruits[l])
                l += 1
            ans = max(ans, r - l + 1)
        return ans








