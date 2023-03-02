# -*- coding: utf-8 -*-

"""
@File    : minimizeSet.py
@Author  : wenhao
@Time    : 2023/2/10 14:17
@LC      : 2302
"""
import math


class Solution:
    def minimizeSet(self, d1: int, d2: int, u1: int, u2: int) -> int:
        lcm = math.lcm(d1, d2)

        def check(mx: int) -> bool:
            # arr1 中能够独占的数 mx // d2 - mx // lcm，则还需 left1 个数
            left1 = max(u1 - (mx // d2 - mx // lcm), 0)
            # arr2 中能够独占的数 mx // d1 - mx // lcm，则还需 left2 个数
            left2 = max(u2 - (mx // d1 - mx // lcm), 0)
            # 现在可以选的公共的数 mx - (mx // d2 + mx // d1 - mx // lcm)
            common = mx - (mx // d2 + mx // d1 - mx // lcm)
            return common >= left1 + left2  # 能选的数必须等于多于要选的数

        # 闭区间二分模板
        l, r = 1, (u1 + u2) * 2 - 1
        while l <= r:
            m = l + (r - l) // 2
            if check(m):
                r = m - 1
            else:
                l = m + 1
        return l












