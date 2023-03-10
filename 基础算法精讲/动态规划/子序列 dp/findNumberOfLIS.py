# -*- coding: utf-8 -*-

"""
@File    : findNumberOfLIS.py
@Author  : wenhao
@Time    : 2023/3/9 16:05
@LC      : 673
"""
from typing import List


class Solution:
    # 这个题目还是很有意思的 😁
    # dp 不止和一个数组相关 这里就用到了 2 个数组进行 dp
    # 感觉是 300 的变形 先求出 以每个字符结尾的最大严格递增子序列的长度
    # 然后统计最大值的个数
    # 递推写法
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        f = [0] * n  # 最长递增子序列的个数
        l = [0] * n  # 最长递增子序列的长度
        for i in range(n):
            cnt = 1  # 子序列的个数
            mx = 0  # 子序列的长度
            for j in range(i):
                if nums[j] < nums[i]:
                    if mx == l[j]:
                        cnt += f[j]
                    elif mx < l[j]:
                        cnt = f[j]
                        mx = l[j]
            f[i] = cnt
            l[i] = mx + 1

        ml = max(l)
        return sum(f[i] if l[i] == ml else 0 for i in range(n))
