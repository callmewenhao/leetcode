# -*- coding: utf-8 -*-

"""
@File    : beautifulSubarrays.py
@Author  : wenhao
@Time    : 2023/3/12 10:04
@LC      : 
"""
from operator import xor
from typing import List
from collections import Counter
from itertools import accumulate


class Solution:
    # 需要把问题转换成 前缀异或和 😂
    # 分析每次操作：子数组中的 2 个数 相同的某一位变成了 0 其余没变
    # 相当于按位 异或 使成对出现的为 1 的位将会变成 0
    # 再考虑前缀异或
    # 如果 pre[i] == pre[j] 则说明原数组 [i, j) 子区间的异或为 0
    # 因为任何一个数异或 0 都不变
    def beautifulSubarrays(self, nums: List[int]) -> int:
        s = list(accumulate(nums, xor, initial=0))  # py 的轮子真好用 😁👍
        print(s)

        ans = 0
        c = Counter()  # 我们遍历全部的 s 元素 不用对 c 进行初始化了
        for x in s:
            ans += c[x]  # c[x] 中的默认值 0
            c[x] += 1
        return ans


    # 走了弯路 😣
    def beautifulSubarrays1(self, nums: List[int]) -> int:
        n = len(nums)
        pre = [0] * (n + 1)

        for i, num in enumerate(nums):
            num = int(f"{num:b}")
            pre[i + 1] = pre[i] + num
            x = pre[i + 1]
            cnt = 0
            while x:
                m = x % 10
                if m % 2:
                    pre[i + 1] -= int(m // 2) * (10 ** cnt)
                else:
                    pre[i + 1] -= int(m) * (10 ** cnt)
                x /= 10
                cnt += 1
        print(pre)
        ans = 0
        c = Counter({0: 1})
        for i in range(1, n + 1):
            if pre[i] in c:
                ans += c[pre[i]]
            c[pre[i]] += 1
        return ans
