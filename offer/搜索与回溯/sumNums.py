# -*- coding: utf-8 -*-

"""
@File    : sumNums.py
@Author  : wenhao
@Time    : 2023/2/7 20:11
@LC      : 
"""


class Solution:
    def sumNums(self, n: int) -> int:
        if n == 1:
            return 1
        return n + self.sumNums(n - 1)




