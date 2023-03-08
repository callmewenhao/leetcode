# -*- coding: utf-8 -*-

"""
@File    : isAnagram.py
@Author  : wenhao
@Time    : 2023/3/7 21:41
@LC      : 242
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sorted(s) 把字符串 s 转变成了一个排序的字符 list
        return sorted(s) == sorted(t)









