# -*- coding: utf-8 -*-

"""
@File    : rotate.py
@Author  : wenhao
@Time    : 2023/2/27 17:19
@LC      : 189
"""
from typing import List
import math

class Solution:
    # 暴力移动是一种方法
    # 时间复杂度优化 反转数组法
    # 向右轮转 == 数组反转 + 左侧反转 k 个 + 右侧反转 (n - k) 个
    # 举一反三 向左轮转 == 数组反转 + 左侧反转 (n - k) 个 + 右侧反转 k 个
    def rotate(self, nums: List[int], k: int) -> None:
        def reverse(nums, l, r):
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

    # 时间优化 环状替换法
    # 为了重新放置一个元素 必然会覆盖一个新元素
    # 所以 我们需要为被覆盖的元素找新位置 直到回到初始位置 可以证明 这是一个环
    # 注意 数组往往需要多个环才能安置好每个元素
    # 具体查看题解
    def rotate1(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n  # 限制 k 的值

        cnt = math.gcd(k, n)  # 最小公倍数
        for i in range(cnt):
            j = i
            prev = nums[i]
            while True:
                j_ = (j + k) % n  # 计算新位置
                if j_ == i:  # 回到了初始位置
                    nums[j_] = prev
                    break
                # 更新值 并保留旧值
                t = nums[j_]
                nums[j_] = prev
                prev = t
                j = j_