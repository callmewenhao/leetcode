# -*- coding: utf-8 -*-

"""
@File    : findTargetSumWays.py
@Author  : wenhao
@Time    : 2023/3/25 20:06
@LC      : 494
"""
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        s = sum(nums) + target
        if s % 2 != 0:
            return 0
        k = s // 2
        # 01 背包 恰好装满的方案数
        f = [[0] * (k + 1) for _ in range(len(nums) + 1)]
        f[0][0] = 1

        for i, num in enumerate(nums):
            for j in range(k + 1):
                if j < num:
                    f[i + 1][j] = f[i][j]
                else:
                    f[i + 1][j] = f[i][j] + f[i + 1][j - num]

        print(f)
        return f[-1][-1]
