# -*- coding: utf-8 -*-

"""
@File    : 1048longestStrChain.py
@Author  : wenhao
@Time    : 2023/4/27 9:22
@LC      : 1048
"""
from typing import List
from functools import cache


class Solution:
    # 翻译成递推
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        f = {}
        for s in words:  # 排序 从小到大遍历
            res = 0
            for i in range(len(s)):
                res = max(res, f.get(s[:i] + s[i + 1:], 0))
            f[s] = res + 1
        return max(f.values())

    # 优化 灵神
    def longestStrChain(self, words: List[str]) -> int:
        ws = set(words)

        @cache
        def dfs(word: str) -> int:
            res = 0
            for i in range(len(word)):
                ns = word[:i] + word[i + 1:]
                if ns in ws:
                    res = max(res, dfs(ns))
            return res + 1

        return max(dfs(word) for word in words)

    # 借用 官解思路
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda p: len(p))

        @cache
        def dfs(i: int) -> int:
            if i < 0: return 0
            res = 0
            for j in range(len(words[i])):
                ns = words[i][:j] + words[i][j + 1:]
                if ns in words:
                    res = max(res, dfs(words.index(ns)))
            return res + 1  # 只能放在这里

        return max(dfs(i) for i in range(len(words)))

    # 自己做法
    # 每次比较 words[j] 是否是 words[i] 的子序列 使用前后缀匹配的办法 1000 * 16
    # 官解是构造 words[i] 的子序列 然后看在不在 words 里面  16 * 1000
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda p: len(p))

        @cache
        def dfs(i: int) -> int:
            if i < 0: return 0
            res = 0
            for j in range(i - 1, -1, -1):
                if len(words[j]) + 1 != len(words[i]):
                    continue

                # 长度符合要求😁
                m = len(words[j])
                # 前缀匹配
                cnt1 = 0
                for k in range(m):
                    if words[i][k] == words[j][k]:
                        cnt1 += 1
                    else:
                        break

                # 后缀匹配
                cnt2 = 0
                for k in range(-1, -m - 1, -1):
                    if words[i][k] == words[j][k]:
                        cnt2 += 1
                    else:
                        break

                if cnt1 + cnt2 >= m:
                    res = max(res, dfs(j))
            return res + 1

        ans = [dfs(x) for x in range(len(words))]
        print(ans)
        return max(ans)
