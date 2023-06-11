# -*- coding: utf-8 -*-

"""
@File    : 2517maximumTastiness.py
@Author  : wenhao
@Time    : 2023/6/1 9:50
@LC      : 2517
"""
from typing import List


class Solution:
    def maximumTastiness(self, p: List[int], k: int) -> int:
        n = len(p)
        p.sort()

        def check(mn: int) -> bool:
            cnt, pre = 1, 0
            for i in range(1, n):
                if p[i] - p[pre] >= mn:
                    cnt += 1
                    pre = i
            return cnt >= k

        left, right = 0, 10 ** 9
        while left <= right:  # 闭区间
            mid = left + (right - left) // 2
            if check(mid):
                left = mid + 1
            else:
                right = mid - 1
        return right
