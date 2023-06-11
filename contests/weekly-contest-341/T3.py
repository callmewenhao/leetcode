# -*- coding: utf-8 -*-

"""
@File    : T3.py
@Author  : wenhao
@Time    : 2023/4/16 10:07
@LC      : 
"""
from functools import cache
from collections import Counter
from itertools import pairwise


class Solution:
    # 方法一 周期字符串
    # 计算需要多少 abc 答案就是目标字符串长度-现在字符串长度
    def addMinimum(self, word: str) -> int:
        cnt = 1
        for i, ch in enumerate(word[1:]):
            if ord(ch) <= ord(word[i]):
                cnt += 1
        return 3 * cnt - len(word)

        # 原来可以这么简单 😭
        # pattern = "abc" * cnt
        #
        # @cache
        # def dfs(i: int, j: int) -> int:
        #     if j < 0:
        #         return i + 1
        #     if word[j] == pattern[i]:
        #         return dfs(i - 1, j - 1)
        #     return dfs(i - 1, j) + 1
        #
        # return dfs(len(pattern) - 1, len(word) - 1)

    # 方法二 计算每两个字符之间应该插入多少字符
    def addMinimum(self, s: str) -> int:
        ans = ord(s[0]) - ord(s[-1]) + 2
        for x, y in pairwise(map(ord, s)):
            ans += (y - x + 2) % 3
        return ans
