# -*- coding: utf-8 -*-

"""
@File    : T3.py
@Author  : wenhao
@Time    : 2023/4/23 9:59
@LC      : 
"""
from typing import List
from collections import Counter
from functools import cache
from itertools import pairwise, accumulate
import heapq


class Solution:
    # 灵神简化版本
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        cnt = [0] * 101  # 数组记录值
        for num in nums[:k - 1]:
            cnt[num] += 1  # 负数就放到后面 灵神太强了😁
        ans = [0] * (len(nums) - k + 1)  # 没有更新就是 0
        for i, (in_, out) in enumerate(zip(nums[k - 1:], nums)):  # 枚举 进入和离开的点
            cnt[in_] += 1  # 进入窗口
            left = x  # 剩余数量
            for j in range(-50, 0):
                left -= cnt[j]
                if left <= 0:  # 满足要求
                    ans[i] = j
                    break
            cnt[out] -= 1  # 离开窗口
        return ans

    # 考虑到数据范围使用 hash + 滑窗  数组代替 hash
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        ans = []
        cnt = [0] * 101

        for i in range(k):
            cnt[nums[i] + 50] += 1

        idx = c = 0
        for i in range(101):
            c += cnt[i]
            if c >= x:
                idx = i - 50
                break
        ans.append(min(idx, 0))

        for i in range(k, len(nums)):
            cnt[nums[i] + 50] += 1
            cnt[nums[i - k] + 50] -= 1
            idx = c = 0
            for j in range(101):
                c += cnt[j]
                if c >= x:
                    idx = j - 50
                    break
            ans.append(min(idx, 0))
        return ans
