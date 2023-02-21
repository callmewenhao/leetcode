# -*- coding: utf-8 -*-

"""
@File    : exchange.py
@Author  : wenhao
@Time    : 2023/1/30 10:22
"""
from typing import List


class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        ans = [val for val in nums if val % 2]
        ans += [val for val in nums if val % 2 == 0]
        return ans
