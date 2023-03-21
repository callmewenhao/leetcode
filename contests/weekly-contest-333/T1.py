# -*- coding: utf-8 -*-

"""
@File    : T1.py
@Author  : wenhao
@Time    : 2023/2/19 10:05
@LC      : 2570
"""
from typing import List
from collections import Counter


class Solution:
    # 灵神 线性做法
    # 充分利用原数组递增顺序排列的性质
    # 分治 双指针
    def mergeArrays(self, a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
        ans = []
        i, n = 0, len(a)
        j, m = 0, len(b)

        while True:
            if i == n:
                ans.extend(b[j:])
                return ans
            if j == m:
                ans.extend(a[i:])
                return ans
            if a[i][0] < b[j][0]:
                ans.append(a[i])
                i += 1
            elif a[i][0] > b[j][0]:
                ans.append(b[j])
                j += 1
            else:
                a[i][1] += b[j][1]
                ans.append(a[i])
                i += 1
                j += 1


    # 比赛时的做法 hashmap
    def mergeArrays1(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        c = Counter()
        for id, val in nums1:
            c[id] += val
        for id, val in nums2:
            c[id] += val

        ans = []
        for k, v in c.items():
            ans.append([k, v])
        ans.sort(key=lambda x: x[0])
        return ans



