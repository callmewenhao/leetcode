# -*- coding: utf-8 -*-

"""
@File    : digitCount.py
@Author  : wenhao
@Time    : 2023/1/11 19:53
"""
from collections import Counter

class Solution:
    def digitCount(self, num: str) -> bool:
        c = Counter(num)
        for i, s in enumerate(num):
            if c[str(i)] != int(s):
                return False
        return True
