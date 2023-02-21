# -*- coding: utf-8 -*-

"""
@File    : change2.py
@Author  : wenhao
@Time    : 2023/2/21 15:20
@LC      : 518
"""
from typing import List


class Solution:
    '''
    给你一个整数数组 coins 表示不同面额的硬币，另给一个整数 amount 表示总金额。
    请你计算并返回可以凑成总金额的硬币组合数。如果任何硬币组合都无法凑出总金额，返回 0 。
    假设每一种面额的硬币有无限个。 🤗 完全背包
    题目数据保证结果符合 32 位带符号整数。
    '''
    # 优化
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        f = [0] * (amount + 1)  # 确定好行 列
        f[0] = 1  #  用 0 组成 0 的方案数是 1

        for i in range(n):
            for j in range(coins[i], amount + 1):
                f[j] = f[j] + f[j - coins[i]]
        return f[amount]

    #
    def change1(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        f = [[0] * (amount + 1) for _ in range(n + 1)]  # 确定好行 列
        f[0][0] = 1

        for i in range(n):
            for j in range(amount + 1):
                if coins[i] > j:
                    f[i + 1][j] = f[i][j]  # 只能用 i 之前的数组成
                else:
                    f[i + 1][j] = f[i][j] + f[i + 1][j - coins[i]]  # 两种组成方案之和
        return f[n][amount]