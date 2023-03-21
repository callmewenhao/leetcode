# -*- coding: utf-8 -*-

"""
@File    : T3.py
@Author  : wenhao
@Time    : 2023/3/19 10:20
@LC      : 
"""
from typing import List
from collections import Counter, defaultdict
from functools import cache


class Solution:
    # 回溯 + 剪枝
    # 子集型回溯时间复杂度 2^n = 2^20 ~ 1e6 😁
    # 当前选的数 x=nums[i]
    # x-k 之前有无选过
    # x+k 之前有无选过
    # 选或者不选的写法
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        ans = -1  # 剪掉空集
        cnt = Counter()

        def dfs(i: int) -> None:
            if i == len(nums):
                nonlocal ans
                ans += 1  # 代表一个子集
                return
            # 选或者不选
            # 不选
            dfs(i + 1)
            # 选
            x = nums[i]
            if cnt[x - k] == 0 and cnt[x + k] == 0:
                cnt[x] += 1
                dfs(i + 1)
                cnt[x] -= 1  # 恢复到递归之前的样子

        dfs(0)
        return ans

    # 动态规划 😂
    # 先来研究 k=1 nums 中无重复元素
    # 考虑最大的数选或者不选
    # - 不选 转变成前 n-1 个数的子问题
    # - 选
    # 最大数 - 次大数 = k 次大数不能选 转变成前 n-2 个数的子问题
    # 最大数 - 次大数 != k 次大数可选 转变成前 n-1 个数的子问题
    # 排序
    # dfs:
    # dfs(i) = dfs(i-1) + dfs(i-2) if nums[i] - nums[i-1] == k
    # dfs(i) = dfs(i-1) * 2 if nums[i] - nums[i-1] != k
    # if i < 0 return 1
    # dfs(n - 1)
    # 处理重复的情况 假设 nums[i] 有 cnt[i] 个
    # dfs:
    # dfs(i) = dfs(i-1) + dfs(i-2) * (pow(2, cnt[i]) - 1) if nums[i] - nums[i-1] == k
    # dfs(i) = dfs(i-1) * pow(2, cnt[i]) if nums[i] - nums[i-1] != k
    # if i < 0 return 1
    # dfs(n - 1)
    # 处理 k 不等于 1 的情况
    # k = 2
    # 奇数一组 偶数一组
    # k = 3
    # 按照 %k 结果分组
    def beautifulSubsets1(self, nums: List[int], k: int) -> int:
        # map[int: map[int: int]]
        groups = defaultdict(Counter)
        for x in nums:
            groups[x % k][x] += 1

        ans = 1
        for cnt in groups.values():
            g = sorted(cnt.items())
            m = len(g)

            @cache
            def dfs(i: int) -> int:
                if i < 0:
                    return 1
                if i == 0:
                    return 1 << g[0][1]
                if g[i][0] - g[i - 1][0] == k:
                    return dfs(i - 1) + dfs(i - 2) * ((1 << g[i][1]) - 1)
                return dfs(i - 1) << g[i][1]

            ans *= dfs(m - 1)
        return ans - 1