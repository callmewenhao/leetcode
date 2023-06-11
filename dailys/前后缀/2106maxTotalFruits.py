# -*- coding: utf-8 -*-

"""
@File    : 2106maxTotalFruits.py
@Author  : wenhao
@Time    : 2023/5/4 9:13
@LC      : 2106
"""
from typing import List
from itertools import accumulate


class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        n = max(fruits[-1][0], startPos + k) + 1
        # 初始化坐标轴
        x = [0] * n
        for i, val in fruits:
            x[i] = val
        # 前缀和数组
        s = list(accumulate(x, initial=0))

        # 找答案
        ans = 0
        left = max(0, startPos - k)
        right = startPos + ((k - startPos) // 2 if k > startPos else 0)
        print(left, right)
        ans = max(ans, s[right + 1] - s[left])
        if k > startPos and (k - startPos) % 2 == 1:
            left += 1
            right += 1

        for _ in range(k // 2 + 1):
            print(left, right)
            left = max(0, left)  # 保护一下
            ans = max(ans, s[right + 1] - s[left])
            left += 2
            right += 1
            if right >= n:
                break

        left = startPos - ((k - (n - 1 - startPos)) // 2 if k > (n - 1 - startPos) else 0)
        right = min(n - 1, startPos + k)
        ans = max(ans, s[right + 1] - s[left])
        if k > (n - 1 - startPos) and (k - (n - 1 - startPos)) % 2 == 1:
            left -= 1
            right -= 1

        for _ in range(k // 2 + 1):
            right = min(n - 1, right)  # 保护一下
            ans = max(ans, s[right + 1] - s[left])
            left -= 1
            right -= 2
            if left < 0:
                break

        return ans
