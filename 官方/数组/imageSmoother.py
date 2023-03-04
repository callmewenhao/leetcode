# -*- coding: utf-8 -*-

"""
@File    : imageSmoother.py
@Author  : wenhao
@Time    : 2023/3/3 10:37
@LC      : 661
"""
from typing import List


class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        n = len(img)
        m = len(img[0])

        ans = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                s = cnt = 0
                for _x in range(-1, 2, 1):
                    for _y in range(-1, 2, 1):
                        x, y = i + _x, j + _y
                        if 0 <= x < n and 0 <= y < m:
                            s += img[x][y]
                            cnt += 1
                ans[i][j] = s // cnt
        return ans
