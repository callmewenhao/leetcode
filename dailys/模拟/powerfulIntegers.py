# -*- coding: utf-8 -*-

"""
@File    : powerfulIntegers.py
@Author  : wenhao
@Time    : 2023/5/2 21:28
@LC      : 970
"""
from typing import List


class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        x_pows, y_pows = [1], [1]
        if x > 1:
            t = x
            while t <= bound:
                x_pows.append(t)
                t *= x
        if y > 1:
            t = y
            while t <= bound:
                y_pows.append(t)
                t *= y
        ans = []
        for xi in x_pows:
            for yi in y_pows:
                if xi + yi > bound:
                    continue
                else:
                    ans.append(xi + yi)
        return list(set(ans))
