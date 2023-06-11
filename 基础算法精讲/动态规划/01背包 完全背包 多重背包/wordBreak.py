# -*- coding: utf-8 -*-

"""
@File    : wordBreak.py
@Author  : wenhao
@Time    : 2023/3/14 9:37
@LC      : 139
"""
from typing import List
from functools import cache


class Solution:
    # 改成二维 dp 写法
    def wordBreak3(self, s: str, wordDict: List[str]) -> bool:
        t = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(n):
            for j in range(0, i + 1):
                if s[j:i + 1] in t and dp[j]:  # 注意 dp 小标和 s 下标意义不通 😁
                    dp[i + 1] = True
        return dp[-1]

    # 记忆化搜索 含 i 写法
    def wordBreak2(self, s: str, wordDict: List[str]) -> bool:
        t = set(wordDict)

        @cache
        def dfs(i: int) -> bool:  # i 代表字符串
            if i < 0:  # 当 i == 0 时代表 还剩空串 返回 true
                return True

            for j in range(0, i + 1):  # 枚举以 i 结尾的字串
                if s[j:i + 1] in t and dfs(j - 1):  # 字串可选且剩余字符串可以组成 则返回 true
                    return True
            return False  # 前面没能返回 true 则返回 false

        return dfs(len(s) - 1)

    # 记忆化搜索 不含 i 写法
    def wordBreak1(self, s: str, wordDict: List[str]) -> bool:
        t = set(wordDict)

        @cache
        def dfs(i: int) -> bool:  # i 代表字符串
            if i == 0:  # 当 i == 0 时代表 还剩空串 返回 true
                return True

            for j in range(0, i):  # 枚举以 i-1 结尾的字串
                if s[j:i] in t and dfs(j):  # 字串可选且剩余字符串可以组成 则返回 true
                    return True
            return False  # 前面没能返回 true 则返回 false

        return dfs(len(s))
