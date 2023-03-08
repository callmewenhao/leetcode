# -*- coding: utf-8 -*-

"""
@File    : canConstruct.py
@Author  : wenhao
@Time    : 2023/3/7 21:34
@LC      : 383
"""


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        c = [0] * 26
        for ch in magazine:
            c[ord(ch) - ord('a')] += 1
        for ch in ransomNote:
            c[ord(ch) - ord('a')] -= 1
            if c[ord(ch) - ord('a')] < 0:
                return False
        return True
