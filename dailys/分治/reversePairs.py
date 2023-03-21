# -*- coding: utf-8 -*-

"""
@File    : reversePairs.py
@Author  : wenhao
@Time    : 2023/3/21 13:13
@LC      : offer 51
"""
from typing import List


class Solution:
    # 经典题目 树状数组 或者 分治（归并排序）
    def reversePairs(self, nums: List[int]) -> int:
        n = len(nums)
        buf = [0] * n

        def mergeSort(nums: List[int], left: int, right: int) -> int:
            if left + 1 >= right:  # 一个数的时候直接返回就行 而不是空区间的时候
                # 大于号 处理空串 😜
                return 0
            res = 0
            mid = (left + right) // 2
            res += mergeSort(nums, left, mid)
            res += mergeSort(nums, mid, right)
            # merge && 计算逆序对个数
            p = left
            i, j = left, mid
            while i < mid and j < right:
                if nums[i] <= nums[j]:
                    buf[p] = nums[i]
                    i += 1
                elif nums[i] > nums[j]:  # else 😁
                    # 计算逆序对
                    res += mid - i
                    # 更新值
                    buf[p] = nums[j]
                    j += 1
                p += 1
            if i < mid:
                buf[p:right] = nums[i:mid]
            if j < right:
                buf[p:right] = nums[j:right]
            nums[left:right] = buf[left:right]
            return res

        return mergeSort(nums, 0, n)
