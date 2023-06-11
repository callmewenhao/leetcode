# -*- coding: utf-8 -*-

"""
@File    : sortPeople.py
@Author  : wenhao
@Time    : 2023/4/25 10:55
@LC      : 2418
"""
from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        a = sorted(enumerate(heights), key=lambda p: p[1], reverse=True)
        return [names[i] for i, _ in a]

