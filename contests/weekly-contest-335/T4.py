# -*- coding: utf-8 -*-

"""
@File    : T4.py
@Author  : wenhao
@Time    : 2023/3/5 20:31
@LC      : 
"""
from typing import List
from functools import cache


class Solution:
    # 分组背包 不是原本意义的多重背包 这个题转换成 01 背包
    # 原问题： n 种题目 组合 target 分的方案数
    # 假设 最后一种题目 n 做了 k 道题
    # 子问题： 前 n - 1 种题目 组合 target - types[n-1][1] * k 分的方案数

    # 递推 一维数组
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7

        f = [0] * (target + 1)
        f[0] = 1  # 初始值 啥也没有时只有组成 0 的方案数是 1
        # 内层循环 反序遍历
        for i, (cnt, marks) in enumerate(types):  # 第 2 行开始遍历
            for j in range(target, -1, -1):  # 反序遍历
                res = 0
                # for 循环中 遍历 k 可能的取值
                # 代表第 i 种物品/题目 选几个
                for k in range(min(cnt, j // marks) + 1):
                    res += f[j - k * marks]  # 递归处理子问题
                f[j] = res % MOD
        return f[-1]

    # 递推 二维数组
    def waysToReachTarget2(self, target: int, types: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        n = len(types)

        f = [[0] * (target + 1) for _ in range(n + 1)]
        f[0][0] = 1  # 初始值 啥也没有时只有组成 0 的方案数是 1
        # 正序循环
        for i, (cnt, marks) in enumerate(types):  # 第 2 行开始遍历
            for j in range(target + 1):  # 还是全部列
                res = 0
                # for 循环中 遍历 k 可能的取值
                # 代表第 i 种物品/题目 选几个
                for k in range(min(cnt, j // marks) + 1):
                    res += f[i][j - k * marks]  # 递归处理子问题
                f[i + 1][j] = res % MOD
        return f[n][target]

    # 记忆化搜索
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        # 使用前 i 种题目 恰好组合 j 分的方案数
        MOD = 10 ** 9 + 7
        n = len(types)

        @cache
        def dfs(i: int, j: int) -> int:
            if i < 0:  # 递归停止的条件
                return 1 if j == 0 else 0
            cnt, marks = types[i]
            # 分析 k 的取值范围
            # j - marks * k >= 0
            # k <= j // marks
            res = 0
            for k in range(min(cnt, j // marks) + 1):
                res += dfs(i - 1, j - k * marks)  # 递归处理子问题
            return res % MOD

        return dfs(n - 1, target)
