# -*- coding: utf-8 -*-

"""
@File    : beautifulSubarrays.py
@Author  : wenhao
@Time    : 2023/2/19 10:06
@LC      : 2572
"""
from typing import List
from collections import Counter

"""
1. 背包的做法
把每个无平方因子数 NSQ 对应的质数集合 表示成一个二进制数

PRIMES = 2, 3, 5, 7, 11, 13, 17, 19, 23, 29
则 6 = {2 3} ==> 0011   一共有 10 个质数 所以这个数顶多用 10 个二进制位
  15 = {3 5} ==> 0110  

转换成 01 背包问题
枚举子集的元素乘积 把乘积看成是一个背包
它去装能够组成这个乘积的 NSQ

2. 状压的做法

直接枚举 NSQ 至多有 30 个
把 NSQ 对应的集合 枚举和 NSQ 没有交集的其他集合
例如 NSQ = 15 = {3 5} 那我们就枚举不包含 {3 5} 的集合



"""
PRIMES = 2, 3, 5, 7, 11, 13, 17, 19, 23, 29  # 一个元组 tuple
NSQ_TO_MASK = [0] * 31

for i in range(2, 31):
    for j, p in enumerate(PRIMES):
        if i % p == 0:
            if i % (p * p) == 0:
                NSQ_TO_MASK[i] = -1
                break
            NSQ_TO_MASK[i] |= 1 << j  # 把第 j 个质数加到 数字集合 中


class Solution:
    # 状压dp
    def squareFreeSubsets(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        MOD = 10 ** 9 + 7
        M = 1 << len(PRIMES)
        f = [0] * M
        f[0] = 1  # 只有一种方案数

        for x, c in cnt.items():  # 枚举不是 1 的 NSQ
            mask = NSQ_TO_MASK[x]
            if mask > 0:
                # 枚举与 mask 没有交集的其余集合 other
                # f[other|mask] += f[other] * c
                # 空间优化 倒序更新
                # 第一种写法 直接枚举 other
                # for other in range(M - 1, -1, -1):
                #     if (other & mask) == 0:
                #         f[other | mask] = (f[other | mask] + f[other] * c) % MOD

                # 第二种写法 枚举补集的子集 包含空集
                other = (M - 1) ^ mask
                s = other
                while True:
                    f[s | mask] = (f[s | mask] + f[s] * c) % MOD
                    s = (s - 1) & other  # 找到下一个子集
                    if s == other:  # 包含 空集 的找子集写法
                        break

        return (sum(f) * pow(2, cnt[1], MOD) - 1) % MOD

    # 01 背包
    # 时间复杂度 O(mn) m=1024
    def squareFreeSubsets(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        M = 1 << len(PRIMES)
        f = [0] * M
        f[0] = 1  # 只有一种方案数
        for x in nums:
            mask = NSQ_TO_MASK[x]
            if mask >= 0:  # 是一个 NSQ
                for j in range(M - 1, mask - 1, -1):
                    # 把 mask 装到一个能容纳 mask 的背包中 j
                    if (mask | j) == j:  # mask 是 j 的子集
                        f[j] = (f[j] + f[mask ^ j]) % MOD  # 不选 mask + 选 mask

        return (sum(f) - 1 + MOD) % MOD  # -1 去掉空集 f[0] == 1
