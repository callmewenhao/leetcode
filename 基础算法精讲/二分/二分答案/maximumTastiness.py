# -*- coding: utf-8 -*-

"""
@File    : maximumTastiness.py
@Author  : wenhao
@Time    : 2023/2/10 15:57
@LC      : 2517
"""
from typing import List


class Solution:
    def maximumTastiness(self, p: List[int], k: int) -> int:
        p.sort()

        def check(mi: int) -> bool:
            cnt = 1
            x0 = p[0]
            for i in range(1, len(p)):
                if p[i] >= x0 + mi:
                    cnt += 1
                    x0 = p[i]
            return cnt >= k

        # 闭区间模板
        # 左端点改成 1 也能过
        l, r = 0, (p[-1] + p[0]) // (k - 1)
        while l <= r:
            m = l + (r - l) // 2
            if check(m):
                l = m + 1
            else:
                r = m - 1
        return l
