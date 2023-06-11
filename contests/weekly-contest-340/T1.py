# -*- coding: utf-8 -*-

"""
@File    : T1.py
@Author  : wenhao
@Time    : 2023/4/9 10:27
@LC      : 
"""
from typing import List
from collections import Counter

# 1 <= nums[i][j] <= 4*106
# 筛质数
MX = 4 * 10 ** 6 + 1
primes = []
is_primes = [False] * (MX + 1)
for i in range(2, MX + 1):
    if not is_primes[i]:
        primes.append(i)
        for j in range(i, MX // i + 1):
            is_primes[i * j] = True


def is_prime(n: int) -> bool:
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return n >= 2


class Solution:
    # 优化
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        ans = 0
        for i, row in enumerate(nums):
            for x in row[i], row[-1 - i]:
                if x > ans and is_prime(x):
                    ans = x
        return ans

    # 比赛代码
    def diagonalPrime1(self, nums: List[List[int]]) -> int:

        # 找最大质数
        ans = 0
        n = len(nums)
        for i in range(n):
            if nums[i][i] in primes:
                ans = max(ans, nums[i][i])
            if nums[i][n - i - 1] in primes:
                ans = max(ans, nums[i][n - i - 1])
        return ans
