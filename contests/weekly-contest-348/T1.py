# -*- coding: utf-8 -*-

"""
@File    : T1.py
@Author  : wenhao
@Time    : 2023/6/4 10:20
@LC      : 
"""
from typing import List
from math import inf
from functools import cache
from itertools import accumulate
from collections import Counter

class Solution:
    def minimizedStringLength(self, s: str) -> int:
        return len(set(s))



