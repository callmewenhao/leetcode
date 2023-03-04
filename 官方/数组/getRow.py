# -*- coding: utf-8 -*-

"""
@File    : getRow.py
@Author  : wenhao
@Time    : 2023/3/3 10:28
@LC      : 119
"""
from typing import List


class Solution:
    def getRow(self, n: int) -> List[int]:
        f = [1] * (n + 1)
        for i in range(1, n + 1):
            prev = f[0]
            for j in range(1, i + 1):
                if j == i:
                    f[j] = 1
                else:
                    t = f[j]
                    f[j] = prev + f[j]
                    prev = t
        return f
