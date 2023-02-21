# -*- coding: utf-8 -*-

"""
@File    : climbStairs.py
@Author  : wenhao
@Time    : 2023/2/10 10:43
@LC      : 70
"""


class Solution:
    # dp 状态压缩写法😁
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        f0 = f1 = 1
        for i in range(2, n + 1):
            f0, f1 = f1, f0 + f1
        return f1










