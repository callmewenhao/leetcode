# -*- coding: utf-8 -*-

"""
@File    : T2.py
@Author  : wenhao
@Time    : 2023/4/23 9:59
@LC      : 
"""


class Solution:
    def sumOfMultiples(self, n: int) -> int:
        ans = 0
        for i in range(1, n + 1):
            if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
                ans += i
        return ans
