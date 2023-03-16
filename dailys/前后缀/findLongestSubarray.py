# -*- coding: utf-8 -*-

"""
@File    : findLongestSubarray.py
@Author  : wenhao
@Time    : 2023/3/11 21:51
@LC      : 
"""
from typing import List
from collections import Counter


class Solution:
    def findLongestSubarray(self, array: List[str]) -> List[str]:
        n = len(array)
        pre = [0] * (n + 1)
        for i, ch in enumerate(array):
            if ch[0].isdigit():
                pre[i + 1] = len(ch) + pre[i]
            else:
                pre[i + 1] = -len(ch) + pre[i]

        start = -1
        max_size = 0
        c = Counter({0: -1})  # value: 前缀和的最左侧坐标
        for i in range(1, n + 1):
            if pre[i] in c:
                if max_size < i - c[pre[i]]:
                    max_size = i - c[pre[i]]
                    start = c[pre[i]] + 1
            else:
                c[pre[i]] = i
        if max_size == 0:
            return []
        return array[start:start + max_size]
