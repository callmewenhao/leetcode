# -*- coding: utf-8 -*-

"""
@File    : T1.py
@Author  : wenhao
@Time    : 2023/3/5 10:10
@LC      : 
"""
from typing import List


class Solution:
    # 找规律 分析数学公式 O1 时间
    def passThePillow(self, n: int, time: int) -> int:
        l = n - 1
        x = time // l
        if (x & 1) == 0:  # 偶数 1->n
            return 1 + (time % l)
        else:  # 奇数 n->1
            return n - (time % l)
