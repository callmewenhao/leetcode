# -*- coding: utf-8 -*-

"""
@File    : getHint.py
@Author  : wenhao
@Time    : 2023/3/13 13:29
@LC      : 299
"""


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        A = 0
        B = [[0] * 2 for _ in range(10)]

        for i, ch in enumerate(secret):
            if ch == guess[i]:
                A += 1
            else:
                B[ord(ch) - ord('0')][0] += 1
                B[ord(guess[i]) - ord('0')][1] += 1
        # return str(A) + 'A' + str(sum(min(B[i][0], B[i][1]) for i in range(10))) + 'B'
        return f"{A}A{sum(min(B[i][0], B[i][1]) for i in range(10))}B"
