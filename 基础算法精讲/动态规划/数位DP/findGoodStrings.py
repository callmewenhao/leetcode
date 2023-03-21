# -*- coding: utf-8 -*-

"""
@File    : findGoodStrings.py
@Author  : wenhao
@Time    : 2023/3/20 22:58
@LC      : 1397
"""
from functools import cache


class Solution:
    # 数位DP + KMP
    # 题目有些难度 看完题解有了很多启发
    # 😁
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        @cache
        def getTrans(stats, ch):
            # 计算 stats 的转移函数
            u = ord(ch) - 97  # ord('a') = 97
            # 下面是 KMP 算法的一部分
            # 把 evil 看作「模式串」，stats 看作「主串」匹配到的位置
            while stats > 0 and evil[stats] != ch:
                stats = fail[stats - 1]
            return stats + 1 if evil[stats] == ch else 0  # 返回匹配的长度

        @cache
        def f(i: int, stats: int, limit: int) -> int:
            if stats == len(evil):
                return 0
            if i == n:
                return 1
            res = 0
            low = ord(s1[i]) if limit & 1 else ord('a')  # 下限
            up = ord(s2[i]) if limit & 2 else ord('z')  # 上限
            for u in range(low, up + 1):
                ch = chr(u)
                next_stats = getTrans(stats, ch)
                next_limit = (ch == s1[i] if limit & 1 else 0) ^ ((ch == s2[i]) << 1 if limit & 2 else 0)
                res += f(i + 1, next_stats, next_limit)
            return res % 1000000007

        m = len(evil)
        fail = [0] * m
        for i in range(1, m):
            j = fail[i - 1]
            while j > 0 and evil[j] != evil[i]:
                j = fail[j - 1]
            if evil[j] == evil[i]:
                fail[i] = j + 1

        return f(0, 0, 3)  # 从 0 开始 长度为 3 上下界都有限制 0011 = 2
