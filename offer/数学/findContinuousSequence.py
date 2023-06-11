# -*- coding: utf-8 -*-

"""
@File    : findContinuousSequence.py
@Author  : wenhao
@Time    : 2023/2/10 22:23
@LC      : 
"""
from typing import List


class Solution:
    # 滑窗，时间复杂度：O(n) 还是没想到😢
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        ans = []
        window = []
        for r in range(1, target):
            window.append(r)
            while sum(window) > target:
                window.pop(0)
            if sum(window) == target:
                ans.append(window.copy())
        return ans




    # 暴力枚举 + 二分、二分答案，时间复杂度：O(n) * O(logn)
    def findContinuousSequence1(self, target: int) -> List[List[int]]:
        ans = []
        for i in range(1, target // 2 + 1):
            l, r = i, target
            while l <= r:
                mid = l + (r - l) // 2
                sum = (i + mid) * (mid - i + 1) // 2
                if sum >= target:
                    r = mid - 1
                else:
                    l = mid + 1
            s = (i + l) * (l - i + 1) // 2
            if s == target:
                ans.append([_ for _ in range(i, l + 1)])
        return ans
