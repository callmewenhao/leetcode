# -*- coding: utf-8 -*-

"""
@File    : hammingWeight.py
@Author  : wenhao
@Time    : 2023/2/8 11:15
@LC      : 
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        while n:
            cnt += 1
            n &= n - 1
        return cnt
