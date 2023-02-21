# -*- coding: utf-8 -*-

"""
@File    : main.py
@Author  : wenhao
@Time    : 2023/1/30 11:38
"""
from itertools import accumulate

grid = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

g_ = list(zip(*grid))

print(g_)  # [(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]
