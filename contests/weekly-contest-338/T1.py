# -*- coding: utf-8 -*-

"""
@File    : T1.py
@Author  : wenhao
@Time    : 2023/3/26 10:16
@LC      : 
"""
from typing import List
from collections import Counter


class Solution:
    # 优化 😂
    def kItemsWithMaximumSum1(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        # if k <= numOnes:
        #     return k
        # if k <= numOnes + numZeros:
        #     return numOnes
        if k <= numOnes + numZeros:
            return min(k, numOnes)
        return numOnes - (k - numOnes - numZeros)

    # 比赛时写了数组写法 😁
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        s = []
        for _ in range(numOnes):
            s.append(1)
        for _ in range(numZeros):
            s.append(0)
        for _ in range(numNegOnes):
            s.append(-1)
        return sum(s[:k])
