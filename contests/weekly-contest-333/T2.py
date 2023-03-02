# -*- coding: utf-8 -*-

"""
@File    : T2.py
@Author  : wenhao
@Time    : 2023/2/19 10:06
@LC      : 2571
"""
import functools

class Solution:
    # 灵神
    # 先考虑最低位的 1 该怎么修改 再考虑高位 这样才能得到最小的操作次数
    # 于是 回溯 枚举是 +2^k 还是 -2^k 其中 2^k = lowbit = x & -x
    # 使用记忆化搜索 优化时间复杂度
    def minOperations(self, n: int) -> int:
        @functools.cache
        def dfs(x: int) -> int:
            # 递归停止的条件
            if x & (x - 1) == 0:  # 判断一个数是否为 2 的幂次
                return 1
            lowbit = x & -x  # 计算 lowbit
            return 1 + min(dfs(x - lowbit), dfs(x + lowbit))  # 最小的加1
        return dfs(n)

    # 比赛做法 贪心 + 递归
    def minOperations1(self, n: int) -> int:
        table = [1] * 18
        for i in range(1, 18):
            table[i] = 2 * table[i - 1]

        def f(n: int):
            if n in table:
                return 1

            l, r = 0, 17
            while l <= r:
                mid = l + (r - l) // 2
                if table[mid] < n:
                    l = mid + 1
                if table[mid] >= n:
                    r = mid - 1

            dif = min(table[l] - n, n - table[r])
            return 1 + f(dif)

        return f(n)









