# -*- coding: utf-8 -*-

"""
@File    : T3.py
@Author  : wenhao
@Time    : 2023/5/21 10:09
@LC      : 
"""

from typing import List
from math import inf
from functools import cache
from itertools import accumulate
from collections import Counter

# 打表预处理😋
ok = [False] * 1001
for i in range(1, 1001):
    s = str(i * i)
    # 回溯写法
    n = len(s)
    sum = 0
    def dfs(p: int) -> bool:
        global sum
        if p == n:
            return sum == i
        x = 0
        for j in range(p, n):
            x = 10 * x + int(s[j])
            sum += x
            if dfs(j + 1): ok[i] = True
            sum -= x
    dfs(0)

class Solution:
    def punishmentNumber(self, n: int) -> int:
        ans = 0
        for i in range(1, n + 1):
            if ok[i]: ans += i * i
        return ans










