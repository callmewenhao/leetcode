# -*- coding: utf-8 -*-

"""
@File    : 1043maxSumAfterPartitioning.py
@Author  : wenhao
@Time    : 2023/4/19 9:40
@LC      : 1043
"""
from typing import List
from functools import cache


class Solution:
    # 经典动态规划 分割数组问题 转换成分割子问题
    # 记搜 时间复杂度 O(n*k)
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        @cache
        def dfs(i: int) -> int:
            # 边界条件
            if i < 0:
                return 0

            res = 0
            mx = 0
            low = max(0, i - k + 1)
            for j in range(i, low - 1, -1):  # 倒序可以实现 边遍历边维护最大值
                mx = max(mx, arr[j])
                res = max(res, mx * (i - j + 1) + dfs(j - 1))
            return res

        return dfs(len(arr) - 1)

    # 翻译成递推
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        f = [0] * (n + 1)  # 状态个数 n+1

        for i in range(n):  # i:0-n
            mx = 0
            for j in range(i, max(i - k, -1), -1):  # j:i->max(i-k,-1)+1 倒叙
                mx = max(mx, arr[j])  # 维护最大值
                f[i + 1] = max(f[i + 1], mx * (i - j + 1) + f[j])  # 更新dp数组

        return f[n]

    # 空间压缩
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        f = [0] * k  # 状态个数 k

        for i in range(n):  # i:0-n
            res = mx = 0
            for j in range(i, max(i - k, -1), -1):  # j:i->max(i-k,-1)+1 倒叙
                mx = max(mx, arr[j])  # 维护最大值
                # f[i + 1] = max(f[i + 1], mx * (i - j + 1) + f[j])  # 更新dp数组
                res = max(res, mx * (i - j + 1) + f[j % k])
            f[(i + 1) % k] = res  # 我们求的是 i+1
        return f[n % k]
