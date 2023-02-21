# -*- coding: utf-8 -*-

"""
@File    : myPow.py
@Author  : wenhao
@Time    : 2023/2/7 21:02
@LC      : 
"""


class Solution:
    # 快速幂
    def myPow(self, x: float, n: int) -> float:

        # 如果底数是 0 直接返回 0
        if x == 0:
            return 0
        # other cases
        res = 1
        if n < 0:  # 负指数
            x = 1 / x
            n = -n

        # 快速幂计算
        while n:
            if n & 1:  # 指数二进制最后一位是 1
                res = res * x  # 结果乘以当前底数
            x *= x  # 底数平方
            n >>= 1  # 指数右移一位
        return res
