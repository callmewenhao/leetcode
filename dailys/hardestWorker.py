# -*- coding: utf-8 -*-

"""
@File    : hardestWorker.py
@Author  : wenhao
@Time    : 2023/1/6 11:42
"""
from typing import List
from itertools import pairwise

class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        ans, t = logs[0]
        for (_, t0), (id, t1) in pairwise(logs):
            if t1 - t0 > t or t1 - t0 == t and ans > id:
                ans, t = id, t1 - t0
        return ans


    def hardestWorker1(self, n: int, logs: List[List[int]]) -> int:
        id, t, end = -1, -1, 0
        for i in logs:
            if i[1] - end > t:
                id = i[0]
                t = i[1] - end
            if i[1] - end == t:
                id = min(id, i[1])
            end = i[1]
        return id
