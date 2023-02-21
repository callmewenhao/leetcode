# -*- coding: utf-8 -*-

"""
@File    : T2.py
@Author  : wenhao
@Time    : 2023/2/19 10:06
@LC      : 6365
"""


class Solution:
    def minOperations(self, n: int) -> int:
        table = [1] * 18
        for i in range(1, 18):
            table[i] = 2 * table[i - 1]

        def f(n: int):
            if n in table:
                return 1

            l, r = 0, 17
            while l <= r:
                mid = l + (r - l) // 2
                if table[mid] < n:
                    l = mid + 1
                if table[mid] >= n:
                    r = mid - 1

            dif = min(table[l] - n, n - table[r])
            return 1 + f(dif)

        return f(n)









