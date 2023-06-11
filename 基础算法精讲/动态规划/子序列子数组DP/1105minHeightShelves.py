# -*- coding: utf-8 -*-

"""
@File    : 1105minHeightShelves.py
@Author  : wenhao
@Time    : 2023/4/19 22:41
@LC      : 1105
"""
from typing import List
from functools import cache
from math import inf


class Solution:
    # 类似分割最大数组DP问题啦😁
    # 记搜
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        @cache
        def dfs(i: int) -> int:
            if i < 0: return 0  # 边界条件
            res = inf
            h = 0
            w = 0  # 记录当前选择的宽度
            for j in range(i, -1, -1):
                if w + books[j][0] <= shelfWidth:
                    # 更新本层 最大高度 和 目前宽度
                    h = max(h, books[j][1])
                    w += books[j][0]
                    # 更新答案
                    res = min(res, h + dfs(j - 1))
                else:  # 不符合要求直接退出
                    break
            return res

        # 答案
        return dfs(len(books) - 1)

    # 改成递推 2 维
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        f = [inf] * (n + 1)
        f[0] = 0  # 边界条件

        for i in range(n):
            h = 0
            w = 0
            for j in range(i, -1, -1):
                if w + books[j][0] <= shelfWidth:
                    w += books[j][0]
                    h = max(h, books[j][1])
                    f[i + 1] = min(f[i + 1], h + f[j])
                else:
                    break
        return f[-1]

