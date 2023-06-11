# -*- coding: utf-8 -*-

"""
@File    : 1072maxEqualRowsAfterFlips.py
@Author  : wenhao
@Time    : 2023/5/15 10:21
@LC      : 1072
"""
from typing import List
from collections import Counter


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        cnt = Counter()
        for row in matrix:
            if row[0]:  # 统一一下 翻转第一个数为 1 的行
                for i in range(n):
                    row[i] ^= 1
            cnt[tuple(row)] += 1
        return max(cnt.values())

