# -*- coding: utf-8 -*-

"""
@File    : T1.py
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
    def minLength(self, s: str) -> int:
        st = []
        for ch in s:
            if st and (ch == 'B' and st[-1] == 'A' or ch == 'D' and st[-1] == 'C') :
                st.pop()
            else: st.append(ch)
        return len(st)




