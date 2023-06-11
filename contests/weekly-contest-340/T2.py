# -*- coding: utf-8 -*-

"""
@File    : T2.py
@Author  : wenhao
@Time    : 2023/4/9 10:27
@LC      : 
"""
from typing import List
from collections import defaultdict
from itertools import accumulate


class Solution:
    # 方法 1
    # 相同元素分组 + 前缀和
    # 神似上周题目
    def distance(self, nums: List[int]) -> List[int]:
        groups = defaultdict(list)
        for i, x in enumerate(nums):
            # 相同元素分组
            groups[x].append(i)
        ans = [0] * len(nums)
        for a in groups.values():
            n = len(a)
            s = list(accumulate(a, initial=0))  # 前缀和
            for j, target in enumerate(a):
                left = target * j - s[j]
                right = s[n] - s[j] - target * (n - j)
                ans[target] = left + right
        return ans

    # 推公式 O1 地计算出对应的值
    def distance(self, nums: List[int]) -> List[int]:
        groups = defaultdict(list)
        for i, x in enumerate(nums):
            # 相同元素分组
            groups[x].append(i)
        ans = [0] * len(nums)
        for a in groups.values():
            n = len(a)
            s = sum(x - a[0] for x in a)
            ans[a[0]] = s
            for i in range(1, n):
                s += (2 * i - n) * (a[i] - a[i - 1])
                ans[a[i]] = s
        return ans

    def distance(self, nums: List[int]) -> List[int]:
        dict = defaultdict(list)
        # -> [n, idx_last_num, |last_num|]
        ans = [0] * len(nums)
        for i, num in enumerate(nums):
            if num not in dict:
                dict[num] = [1, i, 0]
            else:
                dict[num][2] += dict[num][0] * abs(i - dict[num][1])
                dict[num][1] = i
                dict[num][0] += 1
                # 答案
                ans[i] += dict[num][2]
        # <-
        dict.clear()
        for i in range(len(nums) - 1, -1, -1):
            num = nums[i]
            if num not in dict:
                dict[num] = [1, i, 0]
            else:
                dict[num][2] += dict[num][0] * abs(i - dict[num][1])
                dict[num][1] = i
                dict[num][0] += 1
                # 答案
                ans[i] += dict[num][2]
        return ans
