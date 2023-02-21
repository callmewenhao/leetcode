# -*- coding: utf-8 -*-

"""
@File    : findArray.py
@Author  : wenhao
@Time    : 2023/1/6 13:35
"""
from typing import List
from itertools import pairwise


class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        return [pref[0]] + [x ^ y for x, y in pairwise(pref)]
