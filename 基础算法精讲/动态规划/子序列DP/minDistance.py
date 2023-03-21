# -*- coding: utf-8 -*-

"""
@File    : minDistance.py
@Author  : wenhao
@Time    : 2023/2/28 16:31
@LC      : 72
"""
from functools import cache


class Solution:
    # 递推优化 一维数组
    def minDistance3(self, s: str, t: str) -> int:
        n = len(s)

        f = list(range(n + 1))
        for i, x in enumerate(t):
            prev = f[0]  # 注意这里要先记录在修改 😒 被坑了
            f[0] = i + 1
            for j, y in enumerate(s):
                t = f[j + 1]
                if x == y:
                    f[j + 1] = prev
                else:
                    f[j + 1] = min(prev, f[j], f[j + 1]) + 1
                prev = t
        return f[-1]

    # 递推 二维数组
    def minDistance2(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)

        f = [[0] * (n + 1) for _ in range(m + 1)]
        f[0] = [_ for _ in range(n + 1)]

        for i, x in enumerate(t):
            f[i + 1][0] = i + 1
            for j, y in enumerate(s):
                if x == y:
                    f[i + 1][j + 1] = f[i][j]
                else:
                    f[i + 1][j + 1] = min(f[i][j], f[i + 1][j], f[i][j + 1]) + 1
        return f[-1][-1]

    # 记忆化搜索
    def minDistance1(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)

        @cache
        def dfs(i: int, j: int) -> int:
            if i < 0:  # 空串 返回 另一串的长度
                return j + 1
            if j < 0:  # 空串
                return i + 1

            if s[i] == t[j]:
                return dfs(i - 1, j - 1)  # 结尾相等 只考虑前面
            # 不相等 考虑三种操作中的最小值 + 1
            return min(dfs(i - 1, j - 1), dfs(i - 1, j), dfs(i, j - 1)) + 1  # 分别对应 s替换 s删除 s插入

        return dfs(n - 1, m - 1)
