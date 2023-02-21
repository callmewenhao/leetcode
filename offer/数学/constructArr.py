# -*- coding: utf-8 -*-

"""
@File    : constructArr.py
@Author  : wenhao
@Time    : 2023/2/9 10:40
@LC      : 
"""
from typing import List


class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        n = len(a)
        suf_prod = [1] * n
        for i in range(n - 2, -1, -1):
            suf_prod[i] = suf_prod[i + 1] * a[i + 1]

        pre_prod = 1
        ans = [0] * n
        for i in range(0, n):
            ans[i] = pre_prod * suf_prod[i]
            pre_prod *= a[i]
        return ans



