# -*- coding: utf-8 -*-

"""
@File    : maxAverageRatio.py
@Author  : wenhao
@Time    : 2023/2/19 10:14
@LC      : 1792
"""
import heapq
from typing import List
from heapq import heapify


class Entry:
    # 当你事先知道 class 的 attributes 的时候，
    # 建议使用 slots 来节省 memory 以及获得更快的 attribute access
    __slots__ = 'p', 't'

    def __init__(self, p: int, t: int):
        self.p = p
        self.t = t

    def __lt__(self, b: 'Entry') -> bool:
        return (self.t - self.p) * b.t * (b.t + 1) \
               > (b.t - b.p) * self.t * (self.t + 1)


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        h = [Entry(*c) for c in classes]
        heapify(h)

        for _ in range(extraStudents):
            heapq.heapreplace(h, Entry(h[0].p + 1, h[0].t + 1))
        return sum(e.p / e.t for e in h) / len(h)
