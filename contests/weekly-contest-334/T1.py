# -*- coding: utf-8 -*-

"""
@File    : T1.py
@Author  : wenhao
@Time    : 2023/2/26 9:45
@LC      : 
"""
from typing import List


class Solution:
    # 优化空间 On -> O1
    # 有时候没必要求出前后缀数组 只需要一个数字就代表前后缀和就行
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        pre_sum = 0
        suf_sum = sum(nums)
        ans = []
        for i, num in enumerate(nums):
            suf_sum -= num
            diff = abs(pre_sum - suf_sum)
            ans.append(diff)
            pre_sum += num
        return ans


    # 比赛时的做法
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre_sum = [0] * (n + 1)
        for i, num in enumerate(nums, 1):
            pre_sum[i] = pre_sum[i - 1] + num

        suf_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suf_sum[i] = suf_sum[i + 1] + nums[i]

        ans = [0] * n
        for i in range(n):
            ans[i] = abs(pre_sum[i] - pre_sum[i + 1])
        return ans