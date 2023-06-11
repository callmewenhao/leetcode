# -*- coding: utf-8 -*-

"""
@File    : T1.py
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
    def removeTrailingZeros(self, num: str) -> str:
        num = int(num[::-1])
        return str(num)[::-1]



