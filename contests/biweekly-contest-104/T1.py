# -*- coding: utf-8 -*-

"""
@File    : T1.py
@Author  : wenhao
@Time    : 2023/5/13 22:17
@LC      : 
"""
from typing import List
from math import inf
from functools import cache
from itertools import accumulate
from collections import Counter


class Solution:
    def countSeniors(self, details: List[str]) -> int:
        ans = 0
        for detail in details:
            if int(detail[11:13]) > 60:
                ans += 1
        return ans
