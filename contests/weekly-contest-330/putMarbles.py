# -*- coding: utf-8 -*-

"""
@File    : putMarbles.py
@Author  : wenhao
@Time    : 2023/1/29 17:27
"""
from typing import List


class Solution:
    # 使用原数组优化
    def putMarbles(self, wt: List[int], k: int) -> int:
        for i in range(len(wt) - 1):
            wt[i] = wt[i] + wt[i + 1]
        wt.pop()
        wt.sort()
        return sum(wt[len(wt) - k + 1:]) - sum(wt[:k - 1])

    def putMarbles1(self, wt: List[int], k: int) -> int:
        a = [0] * (len(wt) - 1)
        for i in range(len(wt) - 1):
            a[i] = wt[i] + wt[i + 1]
        a.sort()
        return sum(a[len(a) - k + 1:]) - sum(a[:k - 1])
