# -*- coding: utf-8 -*-

"""
@File    : main.py
@Author  : wenhao
@Time    : 2023/1/30 11:38
"""
import math
from typing import List

# 算法设计与分析
# 课堂题目
# 数组的右循环移动
# On 时间复杂度 O1 空间复杂度 算法实现

nums = [1, 2, 3, 4, 5, 6, 7, 8]
nums1 = [-1, -100, 3, 99]


def rotate(nums: List[int], k: int):
    n = len(nums)
    k %= n

    cnt = math.gcd(k, n)
    for i in range(cnt):
        j = i
        prev = nums[i]
        while True:
            j_ = (j + k) % n
            if j_ == i:
                nums[j_] = prev
                break

            t = nums[j_]
            nums[j_] = prev
            prev = t
            j = j_


rotate(nums, 7)
print(nums)

# rotate(nums1, 2)
# print(nums1)
