# -*- coding: utf-8 -*-

"""
@File    : minNumber.py
@Author  : wenhao
@Time    : 2023/2/2 10:57
@LC      : 
"""
from typing import List
from functools import cmp_to_key


class Solution:
    def minNumber(self, nums: List[int]) -> str:
        key = cmp_to_key(lambda x, y: int(x + y) - int(y + x))
        res = ''.join(sorted(map(str, nums), key=key))
        return res
