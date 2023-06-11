# -*- coding: utf-8 -*-

"""
@File    : T2.py
@Author  : wenhao
@Time    : 2023/3/26 10:16
@LC      : 
"""
from typing import List
from bisect import bisect_right, bisect_left

MX = 1000
primes = [0]  # 提前加个 0 防止二分查找下标 -1 越界
is_primes = [True] * MX

for i in range(2, MX):  # 这种写法的好处就是不用多开数组 👏
    if is_primes[i]:
        primes.append(i)
        for j in range(i * i, MX, i):  # 和下面的代码结果一样 😂
            is_primes[j] = False


class Solution:
    # 质数
    # 每个数只操作一次
    # 贪心思想 😁 第一个数减到越小越好
    # nums[0] 减去 < nums[0] 的最大质数
    # 找到一个小于 nums[0] 的最大的数 ==> 经典二分查找 😁
    #
    # 预处理质数
    # 二分找这个数
    def primeSubOperation(self, nums: List[int]) -> bool:

        # j = bisect_left(primes, nums[0]) - 1
        # pre = nums[0] - primes[j]
        # for i in range(1, len(nums)):
        pre = 0  # 优化
        for x in nums:
            if x <= pre:  # 还没减就小于了 返回 False
                return False
            # x - p > pre
            # p < x - pre  # 和上面一样的 😁
            j = bisect_left(primes, x - pre) - 1
            pre = x - primes[j]
        return True

    def primeSubOperation1(self, nums: List[int]) -> bool:
        # 筛质数
        primes = []
        is_primes = [False] * 1010  # 多开一点
        for i in range(2, 1002):  # 1001
            if not is_primes[i]:
                primes.append(i)
                for j in range(i, 1002 // i):  # 1001
                    is_primes[i * j] = True

        # 反着遍历
        for i in range(len(nums) - 2, -1, -1):
            num = nums[i]
            if num < nums[i + 1]:
                continue
            dif = num - nums[i + 1]
            idx = bisect_right(primes, dif)  # 二分、二分答案  暴力枚举应该也能过 😁
            if primes[idx] >= num:
                return False
            nums[i] = num - primes[idx]

        return True
