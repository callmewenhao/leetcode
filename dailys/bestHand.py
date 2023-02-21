# -*- coding: utf-8 -*-

"""
@File    : bestHand.py
@Author  : wenhao
@Time    : 2023/2/20 10:55
@LC      : 2347
"""
from typing import List
from collections import Counter

class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        r = Counter(ranks)
        s = Counter(suits)

        if len(s) == 1:
            return "Flush"
        cnt = 0
        for _, v in r.items():
            cnt = max(cnt, v)
        if cnt >= 3:
            return "Three of a Kind"
        if cnt == 2:
            return "Pair"
        if len(r) == 5:
            return "High Card"
        return ""


