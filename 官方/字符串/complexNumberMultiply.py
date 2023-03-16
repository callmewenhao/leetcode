# -*- coding: utf-8 -*-

"""
@File    : complexNumberMultiply.py
@Author  : wenhao
@Time    : 2023/3/14 11:09
@LC      : 537
"""


class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        num1 = num1.split('+')
        x1, y1 = int(num1[0]), int(num1[1][:-1])

        num2 = num2.split('+')
        x2, y2 = int(num2[0]), int(num2[1][:-1])

        x3 = x1 * x2 - y1 * y2
        y3 = x1 * y2 + x2 * y1

        return f"{x3}+{y3}i"












