# -*- coding: utf-8 -*-

"""
@File    : integerBreak.py
@Author  : wenhao
@Time    : 2023/2/10 22:11
@LC      : 343
"""


class Solution:
    # 尽可能地切成相等的数
    def integerBreak(self, n: int) -> int:
        ans = n - 1
        for i in range(2, n + 1):
            nums = [n // i] * i
            mod = n % i
            for j in range(mod):
                nums[j] += 1
            prod = 1
            for num in nums:
                prod *= num
            ans = max(ans, prod)
        return ans