# -*- coding: utf-8 -*-

"""
@File    : maxAlternatingSum.py
@Author  : wenhao
@Time    : 2023/4/8 20:22
@LC      : 1911
"""
from typing import List
from functools import cache
from math import inf


class Solution:
    # 和股票刚好相似
    # 先买入再卖出 但是买入赚钱 卖出赔钱
    # 求最大利润 答案应该是手里有一个数
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)

        # dfs(i, hold) 含义
        # 第 i 的物品结束时 hold 状态下 能够得到的最大利润
        @cache
        def dfs(i: int, hold: bool) -> int:
            if i < 0:
                return -inf if hold else 0
            if hold:
                return max(dfs(i - 1, True), dfs(i - 1, False) + nums[i])
            return max(dfs(i - 1, False), dfs(i - 1, True) - nums[i])

        return dfs(n - 1, True)  # dfs(n - 1, True) 比 dfs(n - 1, False) 大
