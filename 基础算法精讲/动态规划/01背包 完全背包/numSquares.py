# -*- coding: utf-8 -*-

"""
@File    : numSquares.py
@Author  : wenhao
@Time    : 2023/2/21 15:05
@LC      : 279
"""
import math


class Solution:
    '''
    给你一个整数 n ，返回和为 n 的完全平方数的最少数量
    完全平方数是一个整数，其值等于另一个整数的平方；
    换句话说，其值等于一个整数自乘的积。
    例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。
    🤗 完全背包
    '''
    # 一维数组
    def numSquares(self, n: int) -> int:
        nums = [num ** 2 for num in range(1, 101)]

        f = [math.inf] * (n + 1)
        f[0] = 0  # 注意这里 使用 0 组成 0 使用的数字个数应该是 0，而不是 1

        for i in range(100):
            for j in range(nums[i], n + 1):
                f[j] = min(f[j], f[j - nums[i]] + 1)

        return f[n] if f[n] < math.inf else -1


    def numSquares1(self, n: int) -> int:
        nums = [num ** 2 for num in range(1, 101)]

        f = [[math.inf] * (n + 1) for _ in range(101)]
        f[0][0] = 0  # 注意这里 使用 0 组成 0 使用的数字个数应该是 0，而不是 1

        for i in range(100):
            for j in range(n + 1):
                if nums[i] > j:
                    f[i + 1][j] = f[i][j]
                else:
                    # 使用 完全背包的公式 尤其是 f[i + 1][j - nums[i]] + 1
                    f[i + 1][j] = min(f[i][j], f[i + 1][j - nums[i]] + 1)

        return f[100][n] if f[100][n] < math.inf else -1











