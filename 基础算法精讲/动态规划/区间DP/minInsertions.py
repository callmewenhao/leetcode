# -*- coding: utf-8 -*-

"""
@File    : minInsertions.py
@Author  : wenhao
@Time    : 2023/4/5 20:02
@LC      : 1312
"""
from functools import cache


class Solution:
    # 仔细分析确实经典区间 DP
    """
    和 alice 和 bob 那题很像
    关注 s 的两端
    如果 s[i] s[j] 相等 那只需要把中间的部分变成回文串 dfs(i + 1, j - 1)
    如果 s[i] s[j] 不相等 那分两种情况 插入 i 还是 j 处的字符 返回两种情况的最小值 + 1
    min(dfs(i, j - 1), dfs(i + 1, j)) + 1
    答案就是 dfs(0, n - 1)
    """

    def minInsertions(self, s: str) -> int:
        n = len(s)

        @cache
        def dfs(i: int, j: int) -> int:
            if i >= j:
                return 0

            if s[i] == s[j]:
                return dfs(i + 1, j - 1)
            return min(dfs(i, j - 1), dfs(i + 1, j)) + 1

        return dfs(0, n - 1)

    # 改成递推
    def minInsertions1(self, s: str) -> int:
        n = len(s)
        f = [[0] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            # f[i][i] = 0
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    f[i][j] = f[i + 1][j - 1]
                else:
                    f[i][j] = min(f[i][j - 1], f[i + 1][j]) + 1
        return f[0][n - 1]
