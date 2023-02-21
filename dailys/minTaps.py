# -*- coding: utf-8 -*-

"""
@File    : minTaps.py
@Author  : wenhao
@Time    : 2023/2/21 8:45
@LC      : 1326
"""
from typing import List


class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        right_most = [0] * (n + 1)  # 存储以 i 为起点能达到的最远的右端点
        for i, r in enumerate(ranges):
            left = max(0, i - r)
            right_most[left] = max(right_most[left], i + r)

        ans = 0
        cur_right = 0  # 当前所在的点
        next_right = 0  # 当前所在的点 能达到的右端点
        for i in range(n):
            next_right = max(next_right, right_most[i])  # 贪心地更新 当前所在的点 能达到的最大右端点
            if i == cur_right:  # 从能达到的最大右端点继续向下找
                if i == next_right:  # 无法跨越 i to i + 1
                    return -1
                cur_right = next_right  # 否则可以更新
                ans += 1
        return ans
