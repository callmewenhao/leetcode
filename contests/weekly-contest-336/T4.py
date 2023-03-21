# -*- coding: utf-8 -*-

"""
@File    : repairCars.py
@Author  : wenhao
@Time    : 2023/3/12 10:03
@LC      : 
"""
from typing import List


class Solution:
    # 抄的灵神题解 😊
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x: x[1])
        run = [False] * 2001

        for start, end, d in tasks:
            d -= sum(run[start:end + 1])
            if d > 0:
                for i in range(end, start - 1, -1):
                    if run[i]:
                        continue
                    run[i] = True
                    d -= 1
                    if d <= 0:
                        break

        return sum(run)
