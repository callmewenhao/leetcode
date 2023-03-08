# -*- coding: utf-8 -*-

"""
@File    : NumArray.py
@Author  : wenhao
@Time    : 2023/3/5 15:45
@LC      : 303
"""
from typing import List
from itertools import accumulate


class NumArray:
    def __init__(self, nums: List[int]):
        self.s = list(accumulate(nums, initial=0))

    def sumRange(self, left: int, right: int) -> int:
        return self.s[right + 1] - self.s[left]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
