# -*- coding: utf-8 -*-

"""
@File    : 1016queryString.py
@Author  : wenhao
@Time    : 2023/5/11 9:56
@LC      : 1016
"""


class Solution:
    # 还是得看灵神的分析
    # 精妙之处在于 循环次数的分析
    def queryString(self, s: str, n: int) -> bool:
        return all(bin(i)[2:] for i in range(1, n + 1))  # all 会提前结束
