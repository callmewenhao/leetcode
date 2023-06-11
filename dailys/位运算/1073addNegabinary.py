# -*- coding: utf-8 -*-

"""
@File    : 1073addNegabinary.py
@Author  : wenhao
@Time    : 2023/5/18 18:50
@LC      : 1073
"""
from typing import List


class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        n1, n2 = len(arr1), len(arr2)
        n3 = max(n1, n2) + 2
        arr = [0] * n3
        for i in range(0, n3):
            if i < n1:
                arr[n3 - 1 - i] += arr1[n1 - 1 - i]
            if i < n2:
                arr[n3 - 1 - i] += arr2[n2 - 1 - i]

        for i in range(n3 - 1, 1, -1):
            if arr[i] >= 2:
                if arr[i - 1] == 0:
                    arr[i - 1] += 1
                    arr[i - 2] += 1
                else:
                    arr[i - 1] -= 1
                arr[i] %= 2

        idx = -1
        for i in range(n3):
            if arr[i]:
                idx = i
                break
        if idx == -1: return [0]
        return arr[idx:]

