# -*- coding: utf-8 -*-

"""
@File    : longestDecomposition.py
@Author  : wenhao
@Time    : 2023/4/12 8:47
@LC      : 1147
"""


class Solution:
    # 暴力解法就行
    def longestDecomposition(self, s: str) -> int:
        if s == "":
            return 0
        for i in range(1, len(s) // 2 + 1):  # 枚举前后缀长度 取一半
            if s[:i] == s[-i:]:
                return 2 + self.longestDecomposition(s[i:-i])
        return 1  # 无法分割




















