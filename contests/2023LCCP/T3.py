# -*- coding: utf-8 -*-

"""
@File    : T3.py
@Author  : wenhao
@Time    : 2023/4/22 14:49
@LC      : 
"""
from typing import List
from collections import Counter

class Solution:
    def fieldOfGreatestBlessing(self, forceField: List[List[int]]) -> int:
        mx = 1
        cnt = Counter()
        for x, y, d in forceField:
            #
            x1, y1 = x - d / 2, y + d / 2
            x2, y2 = x + d / 2, y - d / 2
            new_cnt = []
            for ((x_1, y_1), (x_2, y_2)), val in cnt.items():
                new_x1 = max(x_1, x1)
                new_y1 = min(y_1, y1)
                new_x2 = min(x_2, x2)
                new_y2 = max(y_2, y2)
                if new_x1 > new_x2 or new_y1 < new_y2:
                    continue
                new_cnt.append(((new_x1, new_y1), (new_x2, new_y2), val + 1))
                mx = max(mx, val + 1)
            for ((x_1, y_1), (x_2, y_2)), val in new_cnt:
                cnt[((x_1, y_1), (x_2, y_2))] = val
            cnt[((x1, y1), (x2, y2))] += 1
        return mx
