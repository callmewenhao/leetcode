# -*- coding: utf-8 -*-

"""
@File    : 1130mctFromLeafValues.py
@Author  : wenhao
@Time    : 2023/5/31 10:20
@LC      : 1130
"""
from typing import List


class Solution:
    # 贪心 + dfs
    # O(n*(n+n))
    def mctFromLeafValues(self, arr: List[int]) -> int:
        ans = 0

        def dfs(nums: List[int]):
            n = len(nums)
            if n == 1:
                return

            mn_idx = 0
            for i in range(n - 1):
                if nums[i] * nums[i + 1] < nums[mn_idx] * nums[mn_idx + 1]:
                    mn_idx = i

            nonlocal ans
            # print(n, mn_idx)
            ans += nums[mn_idx] * nums[mn_idx + 1]
            dfs(nums[:mn_idx] + [max(nums[mn_idx], nums[mn_idx + 1])] + nums[mn_idx + 2:])

        dfs(arr)
        return ans
