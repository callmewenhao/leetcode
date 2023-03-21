# -*- coding: utf-8 -*-

"""
@File    : T1.py
@Author  : wenhao
@Time    : 2023/3/19 10:20
@LC      : 
"""
from typing import List
from collections import Counter


class Solution:
    # 枚举每个 bit 基本做法 典中典 😁
    # &1 得到最右的一位
    # >>1 右移一位
    def evenOddBit1(self, n: int) -> List[int]:
        ans = [0, 0]  # [偶数 奇数]
        i = 0
        while n:
            ans[i] += n & 1  # 偶数位置是 0 还是 1
            n >>= 1  # 更新 n
            i ^= 1  # 奇偶交换
        return ans

    def evenOddBit(self, n: int) -> List[int]:
        s = f"{n:b}"
        n = len(s)
        odd = even = 0
        for i in range(n):
            if (i & 1) == 0 and s[n - 1 - i] == '1':
                even += 1
            if (i & 1) > 0 and s[n - 1 - i] == '1':
                odd += 1
        return [even, odd]
