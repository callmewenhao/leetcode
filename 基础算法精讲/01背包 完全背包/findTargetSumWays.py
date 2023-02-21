# -*- coding: utf-8 -*-

"""
@File    : findTargetSumWays.py
@Author  : wenhao
@Time    : 2023/2/20 15:55
@LC      : 494
"""
from typing import List
from functools import cache


class Solution:
    # dp 递推写法 优化：使用 1 个数组
    # 为了避免覆盖掉前面的数据，要从右向左更新数组
    def findTargetSumWays3(self, nums: List[int], target: int) -> int:
        target += sum(nums)
        if target < 0 or target % 2:
            return 0
        target //= 2

        f = [0] * (target + 1)
        f[0] = 1  # 边界条件

        for x in nums:
            for c in range(target, x - 1, -1):
                f[c] = f[c] + f[c - x]
        return f[target]

    # dp 递推写法 优化：使用 2 个数组
    def findTargetSumWays3(self, nums: List[int], target: int) -> int:
        target += sum(nums)
        if target < 0 or target % 2:
            return 0
        target //= 2
        n = len(nums)

        # 使用 2 个数组优化空间复杂度
        f = [[0] * (target + 1) for _ in range(2)]
        f[0][0] = 1  # 边界条件

        for i, x in enumerate(nums):
            for c in range(target + 1):
                if c < x:
                    f[(i + 1) % 2][c] = f[i % 2][c]
                else:
                    f[(i + 1) % 2][c] = f[i % 2][c] + f[i % 2][c - x]
        return f[n % 2][target]

    # dp 递推写法
    def findTargetSumWays3(self, nums: List[int], target: int) -> int:
        target += sum(nums)
        if target < 0 or target % 2:
            return 0
        target //= 2
        n = len(nums)
        # 数组的行数代表可选择数的范围  列数代表选择目标值 数组值代表方案数
        # 返回值就是 f[n][target] 即用前 n 行组成 target 的目标数
        f = [[0] * (target + 1) for _ in range(n + 1)]
        f[0][0] = 1  # 边界条件

        for i, x in enumerate(nums):
            for c in range(target + 1):
                if c < x:
                    f[i + 1][c] = f[i][c]
                else:
                    f[i + 1][c] = f[i][c] + f[i][c - x]
        return f[n][target]

    # 记忆化搜索
    def findTargetSumWays2(self, nums: List[int], target: int) -> int:
        # 数字总和是 s
        # 假设添加正号的数之和是 p
        # 则添加负号的数之和是 s - p
        # 则目标等于 p - (s - p) = t
        # 也即 p = (s + t) / 2
        # 问题变成从 nums 中选出一些数字 和为 p 这就是一个 01背包 的变形
        # 也就是：从 nums 中选出一些数 使之和为 p 求选择方案数目
        # dfs(i, p) = dfs(i - 1, p) + dfs(i - 1, p - nums[i])
        # 函数返回值代表方案数 后者需要判断 p 与 nums[i] 的大小关系
        # 边界条件为：if i < 0: return 1 if p == 0 else 0
        target += sum(nums)
        if target < 0 or target % 2:
            return 0
        target //= 2
        n = len(nums)

        @cache  # 记忆化搜索
        def dfs(i: int, p: int) -> int:
            # dfs 边界条件
            if i < 0:
                return 1 if p == 0 else 0
            if nums[i] > p:
                return dfs(i - 1, p)
            return dfs(i - 1, p) + dfs(i - 1, p - nums[i])

        return dfs(n - 1, target)  # 从后向前挑数

    # dfs 暴力枚举 TLE
    def findTargetSumWays1(self, nums: List[int], target: int) -> int:
        n = len(nums)
        ans = 0

        def dfs(i: int, s):
            nonlocal ans
            # 递归停止条件
            if i < 0:
                if s == target:
                    ans += 1
                return

            dfs(i - 1, s + nums[i])  # +
            dfs(i - 1, s - nums[i])  # -

        dfs(n - 1, 0)  # 从最后一个数开始
        return ans
