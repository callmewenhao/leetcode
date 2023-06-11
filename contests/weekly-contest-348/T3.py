# -*- coding: utf-8 -*-

"""
@File    : T3.py
@Author  : wenhao
@Time    : 2023/6/4 10:20
@LC      : 
"""
from typing import List
from math import inf
from functools import cache
from itertools import accumulate
from collections import Counter


class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        rows = set()
        cols = set()
        row_cnt = col_cnt = 0

        ans = 0
        for type, index, val in queries[::-1]:
            # 行
            if type == 0:
                if index in rows:
                    continue
                else:
                    rows.add(index)
                    ans += (n - col_cnt) * val
                    row_cnt += 1
            # 列
            if type == 1:
                if index in cols:
                    continue
                else:
                    cols.add(index)
                    ans += (n - row_cnt) * val
                    col_cnt += 1
        return ans
