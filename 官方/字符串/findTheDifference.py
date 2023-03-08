# -*- coding: utf-8 -*-

"""
@File    : findTheDifference.py
@Author  : wenhao
@Time    : 2023/3/7 11:03
@LC      : 389
"""
import string
from collections import Counter


class Solution:
    # 优化
    # 位运算
    # 将两个字符串拼接成一个字符串，则问题转换成求字符串中出现奇数次的字符
    # 使用异或运算求出这个数
    def findTheDifference(self, s: str, t: str) -> str:
        ans = 0
        for ch in s:
            ans ^= ord(ch) - ord('a')
        for ch in t:
            ans ^= ord(ch) - ord('a')
        return string.ascii_lowercase[ans]

    # 求和
    # 一个字符对应一个数 多出来的字符 正好等于 多出来的值
    def findTheDifference3(self, s: str, t: str) -> str:
        val = sum(ord(ch) - ord('a') for ch in t) - sum(ord(ch) - ord('a') for ch in s)
        return string.ascii_lowercase[val]

    # 计数
    def findTheDifference2(self, s: str, t: str) -> str:
        c1 = [0] * 26
        for ch in s:
            c1[ord(ch) - ord('a')] += 1

        for ch in t:
            c1[ord(ch) - ord('a')] -= 1
            if c1[ord(ch) - ord('a')] < 0:
                return ch

    # 我的做法
    def findTheDifference1(self, s: str, t: str) -> str:
        c1 = Counter(s)
        c2 = Counter(t)
        for k, v in c2.items():
            if v != c1[k]:
                return k
