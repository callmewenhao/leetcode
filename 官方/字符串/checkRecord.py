# -*- coding: utf-8 -*-

"""
@File    : checkRecord.py
@Author  : wenhao
@Time    : 2023/3/9 22:32
@LC      : 551
"""


class Solution:
    def checkRecord(self, s: str) -> bool:
        return s.count('A') < 2 and "LLL" not in s
