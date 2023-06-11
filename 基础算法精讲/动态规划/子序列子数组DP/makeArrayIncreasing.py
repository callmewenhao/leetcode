# -*- coding: utf-8 -*-

"""
@File    : makeArrayIncreasing.py
@Author  : wenhao
@Time    : 2023/4/20 22:14
@LC      : 1187
"""
from typing import List
from functools import cache
from math import inf
from bisect import bisect_left


class Solution:
    # 记搜 选 或者 不选
    def makeArrayIncreasing(self, a: List[int], b: List[int]) -> int:
        b.sort()  # 为能够二分查找 对 b 排序

        # dfs 的含义
        # 使用严格小于 pre 的 b 中的元素
        # 把 a[:i+1] 变成严格递增数组的最小操作次数
        @cache
        def dfs(i: int, pre: int) -> int:
            if i < 0:
                return 0
            res = dfs() if a[i] < pre else inf  # 不替换 a[i]
            k = bisect_left(b, pre) - 1  # 二分、二分答案 b 中小于 pre 的最大数的下标
            if k >= 0:  # a[i] 替换成小于 pre 的最大数
                res = min(res, dfs(i - 1, b[k]) + 1)
            return res

        ans = dfs(len(a) - 1, inf)  # # 假设 a[n-1] 右侧有个无穷大的数
        return ans if ans < inf else -1

    # 枚举选哪个
    # 最小的替换的次数就是 总长度 - 最大的 lis 的长度
    # 记搜
    def makeArrayIncreasing(self, arr1: List[int], b: List[int]) -> int:
        a = arr1 + [inf]
        b = sorted(set(b))

        @cache
        def dfs(i: int) -> int:
            # i = 0 时不会继续递归 返回 1
            k = bisect_left(b, a[i])
            res = 0 if k >= i else -inf  # k < i 元素就不够啦
            if i and a[i - 1] < a[i]:  # 不用替换
                res = max(res, dfs(i - 1))
            for j in range(i - 2, max(i - k - 2, -1), -1):
                if b[k - (i - j - 1)] > a[j]:
                    # a[j+1] 到 a[i-1] 替换成 b[k-(i-j-1)] 到 b[k-1]
                    res = max(res, dfs(j))
            return res + 1

        ans = dfs(len(a) - 1)
        return -1 if ans < 0 else len(a) - ans
    # 1:1 翻译成递推
    def makeArrayIncreasing(self, arr1: List[int], b: List[int]) -> int:
        a = arr1 + [inf]
        b = sorted(set(b))
        n = len(a)
        f = [0] * n
        for i, x in enumerate(a):
            k = bisect_left(b, a[i])
            res = 0 if k >= i else -inf  # k < i 元素就不够啦
            if i and a[i - 1] < x:  # 不用替换
                res = max(res, f[i - 1])
            for j in range(i - 2, max(i - k - 2, -1), -1):
                if b[k - (i - j - 1)] > a[j]:
                    # a[j+1] 到 a[i-1] 替换成 b[k-(i-j-1)] 到 b[k-1]
                    res = max(res, f[j])
            f[i] = res + 1
        return -1 if f[-1] < 0 else n - f[-1]
