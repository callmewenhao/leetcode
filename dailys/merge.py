# -*- coding: utf-8 -*-

"""
@File    : merge.py
@Author  : wenhao
@Time    : 2023/3/5 20:17
@LC      : 56
"""
from typing import List


class Solution:
    def merge(self, ranges: List[List[int]]) -> List[List[int]]:
        ranges.sort()
        ans = [[ranges[0][0], ranges[0][1]]]  # 使用第一个区间初始化就行 😁
        for l, r in ranges:
            if ans[-1][1] < l:
                ans.append([l, r])
            else:
                ans[-1][1] = max(ans[-1][1], r)
        return ans
