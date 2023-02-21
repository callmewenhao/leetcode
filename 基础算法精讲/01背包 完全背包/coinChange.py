# -*- coding: utf-8 -*-

"""
@File    : coinChange.py
@Author  : wenhao
@Time    : 2023/2/20 19:32
@LC      : 322
"""
from typing import List
import math
import functools


class Solution:
    # dp 递推优化



    # dp 递推
    def coinChange(self, coins: List[int], amount: int) -> int:
        f = [math.inf] * (amount + 1)  # 一维数组即可
        f[0] = 0

        for i, x in enumerate(coins):
            for c in range(x, amount + 1):  # c 代表可用的容量
                    f[c] = min(f[c], f[c - x] + 1)
        ans = f[amount]
        return ans if ans < math.inf else -1

    # 记忆化搜索
    def coinChange1(self, coins: List[int], amount: int) -> int:
        n = len(coins)

        @functools.cache
        def dfs(i, c):
            if i < 0:  # 注意这里的边界值是 0 代表硬币数目是 0
                return 0 if c == 0 else math.inf  # 如果找不到组成，则返回 inf
            if c < coins[i]:
                return dfs(i - 1, c)  # 硬币面值太大不能选
            return min(dfs(i - 1, c), dfs(i, c - coins[i]) + 1)  # 返回两种选择中的最小值

        ans = dfs(n - 1, amount)  # 从最后一个向前选
        return ans if ans < math.inf else -1
