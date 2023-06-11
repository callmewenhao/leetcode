# -*- coding: utf-8 -*-

"""
@File    : maskPII.py
@Author  : wenhao
@Time    : 2023/4/1 20:17
@LC      : 831
"""


# name@domain
# to lowercase
# middle char to *****


class Solution:

    def maskEmailAddress(self, s: str) -> str:
        s = s.lower()
        idx = s.find('@')
        return s[0] + "*****" + s[idx - 1:]

    def maskPhoneNumber(self, s: str) -> str:
        s = ''.join(ch if ch.isdigit() else '' for ch in s)
        n = len(s)
        if n == 10:
            return "***-***-" + s[-4:]
        return '+' + "*" * (n - 10) + "-***-***-" + s[-4:]

    def maskPII(self, s: str) -> str:
        if '@' in s:
            return self.maskEmailAddress(s)
        return self.maskPhoneNumber(s)
