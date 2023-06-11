# -*- coding: utf-8 -*-
"""

@File    : smallestSufficientTeam.py
@Author  : wenhao
@Time    : 2023/4/8 15:07
@LC      : 1125
"""
from typing import List
from functools import cache


class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        sid = {s: i for i, s in enumerate(req_skills)}
        n = len(people)
        mask = [0] * n
        for i, skills in enumerate(people):
            for s in skills:
                mask[i] |= 1 << sid[s]

        # dfs(i,j) 表示从前 i 个集合中选择一些集合，并集等于 j，
        # 需要选择的最小集合

        @cache
        def dfs(i: int, j: int) -> int:
            if j == 0:
                return 0  # 背包已满
            if i < 0:
                return (1 << n) - 1  # 没法装满背包，返回全集，这样下面比较集合大小会取更小的
            res = dfs(i - 1, j)  # 不选
            res2 = dfs(i - 1, j & ~mask[i]) | (1 << i)
            return res if res.bit_count() < res2.bit_count() else res2  # 根据 1 的个数返回

        res = dfs(n - 1, (1 << len(req_skills)) - 1)
        return [i for i in range(n) if (res >> i) & 1]  # 所有在 res 中的下标











