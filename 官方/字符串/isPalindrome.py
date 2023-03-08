# -*- coding: utf-8 -*-

"""
@File    : isPalindrome.py
@Author  : wenhao
@Time    : 2023/3/7 9:33
@LC      : 125
"""


class Solution:
    def isPalindrome1(self, s: str) -> bool:
        sgood = "".join(ch.lower() for ch in s if ch.isalnum())
        return sgood == sgood[::-1]

    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        ans = ""
        for c in s:
            if c.isalpha() or c.isdigit():
                ans += c
        return ans == ans[::-1]
