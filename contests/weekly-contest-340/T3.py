# -*- coding: utf-8 -*-

"""
@File    : T3.py
@Author  : wenhao
@Time    : 2023/4/9 10:27
@LC      : 
"""
import bisect
from typing import List
from collections import Counter
from bisect import bisect_left

# 最大化最小值 == 二分答案
# 二分 mx
# 尽量多的选下标对 使得选出来的对数 >= p
# 如果下标不影响答案 那么可以排序
# 贪心 如果前两个数可以选 那么必选
#

class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        # 优化 check 函数
        # 贪心的思想 相邻的元素选或者不选
        def check(mx: int) -> bool:
            cnt = i = 0
            while i < len(nums) - 1:
                if nums[i + 1] - nums[i] <= mx:  # 可以选
                    cnt += 1
                    i += 2
                else:  # 没法选 跳过
                    i += 1
            return cnt >= p

        # 闭区间模板
        l, r = 0, nums[-1] - nums[0]
        while l <= r:
            m = l + (r - l) // 2
            if check(m):
                r = m - 1
            else:
                l = m + 1
        return l

        # 使用 库函数 版本
        # nums.sort()
        # def check(mx: int) -> int:
        #     cnt = i = 0
        #     while i < len(nums) - 1:
        #         if nums[i + 1] - nums[i] <= mx:  # 可以选
        #             cnt += 1
        #             i += 2
        #         else:  # 没法选 跳过
        #             i += 1
        #     return cnt
        #
        # return bisect_left(range(nums[-1] - nums[0]), p, key=check)

