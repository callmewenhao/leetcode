# -*- coding: utf-8 -*-

"""
@File    : T1.py
@Author  : wenhao
@Time    : 2023/2/18 22:19
@LC      : 6359
"""

from typing import List
from collections import Counter
from collections import deque

class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)

        mx = ""
        c = ''
        for i in range(len(s)):
            if s[i] == '9':
                mx += '9'
            elif s[i] != '9':
                if c == '':
                    mx += '9'
                    c = s[i]
                elif c == s[i]:
                    mx += '9'
                else:
                    mx += s[i]

        mi = ""
        c = ''
        for i in range(len(s)):
            if s[i] == '0':
                mi += '0'
            elif s[i] != '0':
                if c == '':
                    mi += '0'
                    c = s[i]
                elif c == s[i]:
                    mi += '0'
                else:
                    mi += s[i]

        return int(mx) - int(mi)














