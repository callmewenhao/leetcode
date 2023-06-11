# -*- coding: utf-8 -*-

"""
@File    : consecutiveNumbersSum.py
@Author  : wenhao
@Time    : 2023/4/21 23:28
@LC      : 829
"""

class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        # 暴力枚举
        ans = 0
        i = 1
        while i * i < 2 * n:
            if i % 2 == 1 and n % i == 0:
                ans += 1
            if i % 2 == 0 and n % i == i // 2:
                ans += 1
            i += 1
        return ans