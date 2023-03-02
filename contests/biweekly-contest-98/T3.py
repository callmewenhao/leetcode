# -*- coding: utf-8 -*-

"""
@File    : T3.py
@Author  : wenhao
@Time    : 2023/2/18 22:20
@LC      : 2568
"""
from typing import List


class Solution:
    # 或运算 越或越大 😂 或运算是最有魅力的运算 😊❤️
    # 从研究 1 得到结论
    # 如果一个数只有一个 bit 位是 1 的话
    # 并且 这些只有一位是 1 的数可以或出其他数字
    # 比如 1=0001 2=0010 4=0100 可以或出 0-7 任意数字
    # 所以 答案就是 缺失的最小的 2 的幂

    # optimize
    # 只用保存 2 的幂次 所以可以使用一个数来存
    # 空间优化到了 O1
    # 缺失的 2 的幂次对应 该数从低到高的第一个 0 即为取反后的 lowbit
    def minImpossibleOR(self, nums: List[int]) -> int:
        mask = 0
        for n in nums:
            if (n & (n - 1)) == 0:  # 判断是不是 2 的幂
                mask |= n  # 记录 1 所在的位
        mask = ~mask  # 取反
        return mask & -mask  # 计算 lowbit

    # 时间 n + log max(num)
    # 空间 n
    def minImpossibleOR1(self, nums: List[int]) -> int:
        # 用 hashmap 优化时间复杂度
        s = set(nums)
        for i in range(32):
            if 1 << i not in s:  # 寻找第一个不在数组中的 2 的幂
                return 1 << i  # 快速计算 2 的幂


