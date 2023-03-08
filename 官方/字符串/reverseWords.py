# -*- coding: utf-8 -*-

"""
@File    : reverseWords.py
@Author  : wenhao
@Time    : 2023/3/7 10:35
@LC      : 557
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(' ')
        for i in range(len(words)):
            words[i] = words[i][::-1]  # 反转字符串只能用切片 或者转成 list 使用 reverse()
        return ' '.join(words)













