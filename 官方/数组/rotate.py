# -*- coding: utf-8 -*-

"""
@File    : rotate.py
@Author  : wenhao
@Time    : 2023/3/3 13:22
@LC      : 189
"""
from typing import List
import math


class Solution:
    # 交换元素
    # 一共遍历 gcd(n, k) 次
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n  # 限制 k 的值
        m = math.gcd(n, k)  # 外层循环的次数

        for i in range(m):
            cur = i
            prev = nums[cur]
            while True:  # 一个 do while 模型 但是每一步要清除干什么
                nex = (cur + k) % n
                if nex == i:
                    nums[nex] = prev
                    break

                t = nums[nex]
                nums[nex] = prev
                cur = nex
                prev = t

    # 反转数组元素做法
    def rotate1(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def reverse(nums: List[int], l: int, r: int):
            while l < r:
                t = nums[l]
                nums[l] = nums[r]
                nums[r] = t
                l += 1
                r -= 1

        n = len(nums)
        k %= n
        reverse(nums, 0, n - 1)
        reverse(nums, 0, k - 1)
        reverse(nums, k, n - 1)
