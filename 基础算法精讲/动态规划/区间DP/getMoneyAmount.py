# -*- coding: utf-8 -*-

"""
@File    : getMoneyAmount.py
@Author  : wenhao
@Time    : 2023/4/4 11:16
@LC      : 375
"""
from math import inf
from functools import cache
from itertools import accumulate


class Solution:
    # 递推 区间 DP 遍历特点
    def getMoneyAmount(self, n: int) -> int:
        f = [[0] * (n + 10) for _ in range(n + 10)]  # 多取几个 防止取边界时出错 感谢三叶姐😁

        for i in range(n, 0, -1):  # i 范围 n -> 1
            f[i][i] = 0
            for j in range(i + 1, n + 1):  # j 范围 i + 1 -> n
                ans = inf
                for k in range(i, j + 1):  # 枚举中间点 k  i -> j
                    res = max(f[i][k - 1], f[k + 1][j]) + k
                    ans = min(ans, res)
                f[i][j] = ans

        return f[1][n]

    # 记搜
    def getMoneyAmount1(self, n: int) -> int:
        @cache
        def dfs(i: int, j: int) -> int:  # 不必要的参数不要给 否则 cache 会记录这个参数 造成时间超时
            if i >= j:
                return 0
            ans = inf
            for k in range(i, j + 1):
                res = max(dfs(i, k - 1), dfs(k + 1, j)) + k
                ans = min(res, ans)
            return ans

        return dfs(1, n)
