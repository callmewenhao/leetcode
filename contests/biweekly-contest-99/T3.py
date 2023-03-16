# -*- coding: utf-8 -*-

"""
@File    : beautifulSubarrays.py
@Author  : wenhao
@Time    : 2023/3/4 22:44
@LC      : 
"""
from typing import List


class Solution:
    # 其实就是 56题 返回合并区间的组数
    # 把区间分成 m 组：不同组之间不相交 组内相交
    # 答案就是 pow(2, m) 仔细考虑这个 2 的幂
    def countWays1(self, ranges: List[List[int]]) -> int:

        ranges.sort()
        n = len(ranges)
        m = 1  # 组数
        mx = ranges[0][1]  # 维护一个右端点最大值
        for i in range(1, n):
            if ranges[i][0] > mx:
                m += 1
            mx = max(mx, ranges[i][1])  # 在这里出错了 😁
        return pow(2, m, 10 ** 9 + 7)  # 快速幂 😁


    # 比赛时做法 dp 求方案数
    def countWays(self, ranges: List[List[int]]) -> int:
        ranges.sort()

        n = len(ranges)
        f = [2] * n
        mx = ranges[0][1]  # 维护一个右端点最大值

        for i in range(1, n):
            if ranges[i][0] <= mx:
                f[i] = f[i - 1]
            else:
                f[i] = f[i - 1] * 2
            mx = max(mx, ranges[i][1])

        return f[n - 1] % (10 ** 9 + 7)
