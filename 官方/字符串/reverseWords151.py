# -*- coding: utf-8 -*-

"""
@File    : reverseWords151.py
@Author  : wenhao
@Time    : 2023/3/7 10:46
@LC      : 151
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(reversed(s.split()))
