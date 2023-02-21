# -*- coding: utf-8 -*-

"""
@File    : decodeMessage.py
@Author  : wenhao
@Time    : 2023/2/1 10:52
@LC      : 2325
"""
from string import ascii_lowercase

class Solution:
    # optim
    def decodeMessage(self, key: str, message: str) -> str:
        map = {' ': ' '}
        i = 0
        for ch in key:
            if ch not in map:
                map[ch] = ascii_lowercase[i]
                i += 1
        return ''.join(map[ch] for ch in message)


    def decodeMessage1(self, key: str, message: str) -> str:
        table = [''] * 26
        idx = 0
        for ch in key:
            if ch == ' ' or table[ord(ch) - ord('a')] != '':
                continue
            table[ord(ch) - ord('a')] = chr(idx + ord('a'))
            idx += 1
        ans = ""
        for ch in message:
            if ch == ' ':
                ans += ' '
            else:
                ans += table[ord(ch) - ord('a')]
        return ans
