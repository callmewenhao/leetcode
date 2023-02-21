# -*- coding: utf-8 -*-

"""
@File    : reverseWords.py
@Author  : wenhao
@Time    : 2023/1/30 10:31
"""


class Solution:
    # optimize
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.strip().split()[::-1])

    def reverseWords1(self, s: str) -> str:
        ans = ""
        a = s.split(' ')
        a.reverse()
        for w in a:
            if w:
                ans += w
                ans += ' '

        return ans[:-1]
