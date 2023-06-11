# -*- coding: utf-8 -*-

"""
@File    : longestArithSeqLength.py
@Author  : wenhao
@Time    : 2023/4/22 10:41
@LC      : 1027
"""
from typing import List
from functools import cache
from bisect import bisect_right

class Solution:
    def longestArithSeqLength(self, a: List[int]) -> int:
        @cache  # 缓存装饰器，避免重复计算 dfs 的结果
        def dfs(i: int) -> dict[int, int]:
            # i=0 时不会进入循环，返回空哈希表
            max_len = {}
            for j in range(i - 1, -1, -1):
                d = a[i] - a[j]  # 公差
                if d not in max_len:
                    max_len[d] = dfs(j).get(d, 1) + 1
            return max_len
        return max(max(dfs(i).values()) for i in range(1, len(a)))

