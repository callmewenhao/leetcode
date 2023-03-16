# -*- coding: utf-8 -*-

"""
@File    : rk.py
@Author  : wenhao
@Time    : 2023/3/15 18:36
@LC      : 
"""
from typing import List
import math

# 暴力贪心做法
def findMinSumTime(nums: List, target: int) -> int:
    nums.sort(reverse=True)

    ans = 0
    t = target
    for num in nums:
        if num > t:
            continue
        ans += t // num
        t = t % num

    return ans






# dp 做法
def findMinSumTime1(nums: List, target: int) -> int:
    n = len(nums)
    dp = [[math.inf] * (target + 1) for _ in range(n + 1)]
    dp[0][0] = 0

    for i in range(n):
        for j in range(target + 1):
            if nums[i] > j:
                dp[i + 1][j] = dp[i][j]
            else:
                dp[i + 1][j] = min(dp[i + 1][j - nums[i]] + 1, dp[i][j])
    return int(dp[-1][-1])


target = 20
nums = [5, 2, 3, 20]  # 1
nums1 = [5, 2]  # 4
nums2 = [2, 1, 3]  # 7

res = findMinSumTime(nums, target)
print(res)
