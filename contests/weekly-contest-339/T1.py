# -*- coding: utf-8 -*-

"""
@File    : T1.py
@Author  : wenhao
@Time    : 2023/4/2 10:29
@LC      : 
"""
from typing import List
from collections import Counter
from itertools import pairwise


class Solution:
    # 正常双指针 ✔️
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        ans = pre = cur = 0
        for i, ch in enumerate(s):
            cur += 1  # 每个字符 当前指针 + 1
            if i == len(s) - 1 or ch != s[i + 1]:
                if ch == '1':  # 遇到 1 就更新答案
                    ans = max(ans, min(pre, cur) * 2)
                pre = cur  # 更新指针
                cur = 0
        return ans

        # 比赛时偷懒了 😂

    def findTheLongestBalancedSubstring1(self, s: str) -> int:
        slices = []

        start = 0
        for i, ch in enumerate(s):
            if ch != s[start]:
                slices.append(s[start:i])
                start = i
        slices.append(s[start:])
        print(slices)

        ans = 0
        for x, y in pairwise(slices):
            if x[0] == '0':
                ans = max(ans, 2 * min(len(x), len(y)))
        return ans
