# -*- coding: utf-8 -*-

"""
@File    : T1.py
@Author  : wenhao
@Time    : 2023/2/5 10:01
@LC      : 
"""
from typing import List
from collections import Counter
from math import sqrt
from sortedcontainers import SortedList
import heapq


class Solution:
    # optimize
    def pickGifts(self, gifts: List[int], k: int) -> int:
        # 构造最大堆
        for i in range(len(gifts)):
            gifts[i] = -gifts[i]
        heapq.heapify(gifts)
        for _ in range(k):
            if -gifts[0] == 1:
                break  # 如果最大的为 1 就直接返回即可
            heapq.heapreplace(gifts, -int((-gifts[0]) ** 0.5))
        return -sum(gifts)

    def pickGifts1(self, gifts: List[int], k: int) -> int:
        s = SortedList(gifts)
        for _ in range(k):
            num = s.pop()
            s.add(int(sqrt(num)))

        return sum(s)
