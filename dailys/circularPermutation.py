# -*- coding: utf-8 -*-

"""
@File    : circularPermutation.py
@Author  : wenhao
@Time    : 2023/2/23 16:32
@LC      : 1238
"""
from typing import List


class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        ans = [0] * (1 << n)  # 一共 2^n 个数
        for i in range(1 << n):
            # 挨个构造 在 gray码 的基础上异或 start
            ans[i] = start ^ (i >> 1) ^ i
        return ans









