# -*- coding: utf-8 -*-

"""
@File    : T3.py
@Author  : wenhao
@Time    : 2023/4/2 10:29
@LC      : 
"""
from typing import List
from collections import Counter


class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        reward = sorted(zip(reward1, reward2), key=lambda p: (p[0]-p[1]))
        return sum(x2 for x2, _ in reward[:k]) + sum(x1 for _, x1 in reward[k:])




























    # 优化
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        a = sorted(zip(reward1, reward2), key=lambda p: p[1] - p[0])  # 注意是 1-0
        return sum(x[0] for x in a[:k]) + sum(x[1] for x in a[k:])

    # 本以为自己的做法够简洁了，没想到做了小丑 😁
    def miceAndCheese1(self, reward1: List[int], reward2: List[int], k: int) -> int:
        diffs = [x - y for x, y in zip(reward1, reward2)]
        diffs = sorted(enumerate(diffs), key=lambda p: p[1], reverse=True)
        # print(diffs)

        idxs = [diffs[i][0] for i in range(k)]
        ans = sum(reward1[i] for i in idxs) + sum(reward2) - sum(reward2[i] for i in idxs)
        return ans
