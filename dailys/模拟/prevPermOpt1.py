# -*- coding: utf-8 -*-

"""
@File    : prevPermOpt1.py
@Author  : wenhao
@Time    : 2023/4/3 11:04
@LC      : 1053
"""
"""

如果 arr 是有序的 那么就返回原数组 arr
如果 arr 是无序的

贪心
从后向前 找第一个拐点
没有拐点 返回元素组
交换拐点 和 右侧最大的比拐点小的数 得到答案 😁


"""

from typing import List


class Solution:
    # 遍历两遍
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        idx = -1
        n = len(arr)
        for i in range(n - 2, -1, -1):
            if arr[i] > arr[i + 1]:
                idx = i
                break
        if idx == -1:
            return arr
        mx_idx = idx + 1
        for i in range(i + 1, n):
            if arr[mx_idx] < arr[i] < arr[idx]:
                mx_idx = i

        arr[idx], arr[mx_idx] = arr[mx_idx], arr[idx]
        return arr
