# -*- coding: utf-8 -*-

"""
@File    : checkPossibility.py
@Author  : wenhao
@Time    : 2023/3/2 22:22
@LC      : 665
"""
from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        # 一次遍历 判断是否有序
        def isSorted(nums: List[int]) -> bool:
            for i in range(len(nums) - 1):
                if nums[i] > nums[i + 1]:
                    return False
            return True
        # 寻找第一个 非递减的元素对
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                t = nums[i + 1]
                # 后面的元素 +
                nums[i + 1] = nums[i]
                if isSorted(nums):
                    return True
                # 前面的元素 -
                nums[i + 1] = t  # 恢复原来的值
                nums[i] = t
                return isSorted(nums)
        return True
