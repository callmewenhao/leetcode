# -*- coding: utf-8 -*-

"""
@File    : lengthOfLastWord.py
@Author  : wenhao
@Time    : 2023/3/7 9:58
@LC      : 58
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])





