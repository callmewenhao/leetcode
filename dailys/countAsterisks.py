# -*- coding: utf-8 -*-

"""
@File    : countAsterisks.py
@Author  : wenhao
@Time    : 2023/1/29 13:37
"""


class Solution:
    # 一行代码
    def countAsterisks(self, s: str) -> int:
        return sum(t.count('*') for t in s.split('|')[::2])


    def countAsterisks1(self, s: str) -> int:
        ans = 0
        cnt = 0
        for c in s:
            if c == '|':
                cnt += 1
            if cnt % 2 == 0 and c == '*':
                ans += 1
        return ans
