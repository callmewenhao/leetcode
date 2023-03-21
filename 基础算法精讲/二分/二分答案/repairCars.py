# -*- coding: utf-8 -*-

"""
@File    : repairCars.py
@Author  : wenhao
@Time    : 2023/3/20 9:35
@LC      : 
"""
from typing import List
from math import floor, sqrt


class Solution:
    # r * n * n 单调函数
    # 二分答案需要单调性
    # 如果 t 时间能够完成 那么 t+1 t+2 t+3 ... 都能完成
    # 如果 t 时间不能够完成 那么 t-1 t-2 t-3 ... 也不能完成
    # 可以二分答案
    # r * n * n <= t  =>  n <= floor(sqrt(t//r))
    # sum(n) >= cars 说明可以用 t 时间完成
    # 突然发出现还挺简单 😢
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def check(t: int) -> bool:
            s = 0
            for r in ranks:
                s += floor(sqrt(t // r))
            return s >= cars

        # 闭区间模板
        left, right = 0, min(ranks) * cars * cars  # 决定上下界
        while left <= right:
            mid = left + (right - left) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left

        # # 开区间二分模板
        # left, right = 0, min(ranks) * cars * cars  # 决定上下界
        # while left + 1 < right:
        #     mid = left + (right - left) // 2
        #     if check(mid):
        #         right = mid
        #     else:
        #         left = mid
        # return right  # 开区间 返回 right
