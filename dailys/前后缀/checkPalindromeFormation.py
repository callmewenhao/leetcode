# -*- coding: utf-8 -*-

"""
@File    : checkPalindromeFormation.py
@Author  : wenhao
@Time    : 2023/3/18 20:32
@LC      : 1616
"""


class Solution:
    # 自己题目理解失误 🤣
    # 还是看的灵神解法
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        # 判断 a 前缀 + b 后缀是否可以组成回文串
        def check(a: str, b: str) -> bool:
            i, j = 0, len(a) - 1  # 相向双指针
            while i < j and a[i] == b[j]:
                i += 1
                j -= 1
            s, t = a[i: j + 1], b[i: j + 1]
            return s == s[::-1] or t == t[::-1]

        return check(a, b) or check(b, a)
