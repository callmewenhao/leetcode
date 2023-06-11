# -*- coding: utf-8 -*-

"""
@File    : T3.py
@Author  : wenhao
@Time    : 2023/5/7 14:19
@LC      : 
"""
from typing import List
from collections import Counter, defaultdict
from itertools import accumulate, pairwise
from functools import cache
from math import inf


class Solution:
    def extractMantra(self, matrix: List[str], mantra: str) -> float | list[float]:
        n = len(matrix)
        m = len(matrix[0])
        l = len(mantra)  # 1-l

        cnt1 = defaultdict(list)
        for i in range(l):
            cnt1[mantra[i]].append(i + 1)

        # for i in range(1, l+1):
        #     print(cnt1[mantra[i - 1]])

        cnt2 = defaultdict(list)
        cnt2[0].append([0, 0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j] in cnt1:
                    for p in cnt1[matrix[i][j]]:
                        cnt2[p].append([i, j])

        # for i in range(1, l+1):
        #     print(cnt2[i])

        dis = [[inf] * m for _ in range(n)]
        for x3, y3 in cnt2[1]:
            dis[x3][y3] = min(dis[x3][y3], abs(x3) + abs(y3))

        for i in range(1, l):
            for x1, y1 in cnt2[i]:
                if len(cnt2[i + 1]) == 0: return -1
                for x2, y2 in cnt2[i + 1]:
                    dis[x2][y2] = min(dis[x2][y2], dis[x1][y1] + abs(x1 - x2) + abs(y1 - y2))
                    print(matrix[x2][y2], dis[x2][y2])

        ans = min(dis[x][y] for x, y in cnt2[l])
        return ans + l if ans < inf else -1