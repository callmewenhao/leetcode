# -*- coding: utf-8 -*-

"""
@File    : T2.py
@Author  : wenhao
@Time    : 2023/7/2 10:21
@LC      : 
"""
from typing import List

N = 10**6+7
isPrime = [True] * N

for i in range(2, N):
    if isPrime[i]:
        for j in range(2*i, N, i):
            isPrime[j] = False

# print(isPrime)

class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        ans = []
        s = set()

        for i in range(2, n+1):
            if isPrime[i]:
                s.add(i)
                if n - i in s:
                    ans.append([n-i, i])

        return sorted(ans)



