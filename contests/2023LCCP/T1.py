# -*- coding: utf-8 -*-

"""
@File    : T1.py
@Author  : wenhao
@Time    : 2023/4/22 14:49
@LC      : 
"""
from typing import List
from itertools import pairwise


class Solution:
    def supplyWagon(self, supplies: List[int]) -> List[int]:
        arr = supplies
        n = len(supplies)
        t = n - n // 2
        for _ in range(t):
            idx = 0
            for i in range(1, len(arr) - 1):
                if arr[i] + arr[i + 1] < arr[idx] + arr[idx + 1]:
                    idx = i
            new_arr = [0] * (len(arr) - 1)
            new_arr[:idx] = arr[:idx]
            new_arr[idx] = arr[idx] + arr[idx+1]
            new_arr[idx+1:] = arr[idx+2:]
            arr = new_arr
        return arr
