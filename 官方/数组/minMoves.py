# -*- coding: utf-8 -*-

"""
@File    : minMoves.py
@Author  : wenhao
@Time    : 2023/2/15 22:59
@LC      : 453
"""

from typing import List


class Solution:
    # 可恶的数学题 😣
    # 正难则反 😂
    # 原问题等价于： 每次把最大值减一，直到所有元素都等于最小值
    def minMoves(self, nums: List[int]) -> int:
        mi = min(nums)
        ans = 0
        for num in nums:
            ans += num - mi
        return ans








