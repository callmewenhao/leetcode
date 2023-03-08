# -*- coding: utf-8 -*-

"""
@File    : T2.py
@Author  : wenhao
@Time    : 2023/3/4 22:20
@LC      : 
"""
from typing import List
# 其实是等差数列求和
# 1  1 4    1 4 8    1 4 8 12
def coloredCells1(self, n: int) -> int:
    return 1 + 2 * n * (n - 1)


# 比赛时写法 类似 DP
# 比较 n 与 n+1 多了哪些格子
def coloredCells(self, n: int) -> int:
    if n == 1:
        return 1
    f = 1
    for i in range(2, n + 1):
        f = f + i * 4 - 4
    return f
