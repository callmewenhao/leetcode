# -*- coding: utf-8 -*-

"""
@File    : T4.py
@Author  : wenhao
@Time    : 2023/4/23 11:17
@LC      : 
"""
from typing import List
from collections import Counter
from functools import cache
from itertools import pairwise, accumulate
from math import gcd


class Solution:
    # 灵神优化
    def minOperations(self, nums: List[int]) -> int:
        if gcd(*nums) > 1:
            return -1
        n = len(nums)
        cnt1 = sum(x == 1 for x in nums)
        if cnt1:
            return n - cnt1

        min_size = 0
        a = []
        for i, x in enumerate(nums):
            a.append([x, i])
            # 原地去重，因为相同的 GCD 都相邻在一起
            j = 0
            for p in a:
                p[0] = gcd(p[0], x)
                if p[0] != a[j][0]:
                    j += 1
                    a[j] = p
                else:
                    a[j][1] = p[1]
            del a[j + 1:]
            if a[0][0] == 1:
                # 这里本来是 i-a[0][1]+1，把 +1 提出来合并到 return 中
                min_size = min(min_size, i - a[0][1])
        return min_size + n - 1

    # 暴力寻找 gcd
    def minOperations(self, nums: List[int]) -> int:
        step = 0
        if 1 in nums:
            return len(nums) - nums.count(1)
        g = nums
        while g:
            new_g = []
            step += 1
            for i in range(len(g) - 1):
                new_g.append(gcd(g[i], g[i + 1]))
            g = new_g
            if all(num % 2 == 0 for num in g):
                return -1
            if 1 in g:
                break
        return len(nums) - 1 + step
