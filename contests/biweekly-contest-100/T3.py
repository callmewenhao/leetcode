# -*- coding: utf-8 -*-

"""
@File    : T3.py
@Author  : wenhao
@Time    : 2023/3/18 23:21
@LC      : 
"""
from typing import List
from collections import Counter


class Solution:
    # 经典下标排序 😁
    # py 可以用 enumerate() 构造 tuple 对 然后排序
    # 优化 👍
    def findScore(self, nums: List[int]) -> int:
        ans = 0
        vis = [False] * (len(nums) + 2)  # 多开几个空间 保证下标不越界
        for i, x in sorted(enumerate(nums), key=lambda p: p[1]):
            if not vis[i]:
                # vis[i] = True  # 可以不用的 访问过的位置不会再访问 😂
                vis[i - 1] = True
                vis[i + 1] = True
                ans += x
        return ans

    def findScore1(self, nums: List[int]) -> int:
        n = len(nums)
        idx = [_ for _ in range(n)]
        arr = list(zip(nums, idx))
        arr.sort(key=lambda x: x[0])
        vis = [False] * n
        ans = 0
        for (x, idx) in arr:
            if vis[idx]:
                continue
            ans += x
            vis[idx] = True
            if idx - 1 >= 0:
                vis[idx - 1] = True
            if idx + 1 < n:
                vis[idx + 1] = True
        return ans
