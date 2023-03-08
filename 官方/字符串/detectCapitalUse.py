# -*- coding: utf-8 -*-

"""
@File    : detectCapitalUse.py
@Author  : wenhao
@Time    : 2023/3/6 20:09
@LC      : 520
"""


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        n = len(word)
        cnt_C = 0
        for c in word:
            if str.isupper(c):
                cnt_C += 1
        if cnt_C == 0 or cnt_C == n:
            return True
        if cnt_C == 1 and str.isupper(word[0]):
            return True
        return False
