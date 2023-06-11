# -*- coding: utf-8 -*-

"""
@File    : arithmeticTriplets.py
@Author  : wenhao
@Time    : 2023/3/31 9:09
@LC      : 2367
"""
from typing import List
from bisect import bisect_left


class Solution:
    # hash 表
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        s = set(nums)
        return sum(num - diff in s and num + diff in s for num in nums)  # 对 bool 值求和

    # 二分、二分答案
    def arithmeticTriplets1(self, nums: List[int], diff: int) -> int:
        n = len(nums)

        ans = 0
        for i in nums:
            j = i + diff
            if (i1 := bisect_left(nums, j)) == n or nums[i1] != j:
                continue
            k = j + diff
            if (i2 := bisect_left(nums, k)) == n or nums[i2] != k:
                continue
            ans += 1
        return ans
