# -*- coding: utf-8 -*-

"""
@File    : T3.py
@Author  : wenhao
@Time    : 2023/4/1 22:21
@LC      : 
"""

"""
数论知识 😁

1. 每个长度为 k 的子数组的元素总和都相等
  a[i] + a[i+1] + ... + a[i+k-1]
= a[i+1] + a[i+2] + ... + a[i+k]

==> a[i] = a[i+k]
==> a[0] = a[k] = a[2*k] = ...
    a[1] = a[1 + k] = a[1 + 2*k] = ...
    ...

如果不是循环数组，那么 a[0] 这一组和 a[1] 这一组是互不相干的
让一组元素相同，最少需要操作多少次
答案：取所有数到这个组的中位数是最优的，距离之和最小

剩余处理可以用 vis 数组暴力 也可以并查集 灵神使用数论工具👍

a 有一个周期 n
a 有一个周期 k
则 a 还有一个周期 gcd(n, k)  最小正周期
证明：a[i] = a[i + k*x] = a[i + k*x + n*y] = a[i + gcd(n, k)]  
裴蜀定理 k*x + n*y = gcd(n, k)  这是可以构造的 😂
可以通过辗转相除法，构造 x 和 y
==> 数论 裴蜀定理
"""
from typing import List
from collections import Counter
from math import gcd


class Solution:
    def makeSubKSumEqual(self, arr: List[int], k: int) -> int:
        k = gcd(k, len(arr))
        ans = 0

        for i in range(k):
            b = sorted(arr[i::k])  # 排序寻找中位数
            mid = b[len(b) // 2]
            ans += sum(abs(x - mid) for x in b)  # 中位数距离之和
        return ans


