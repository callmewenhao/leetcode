# -*- coding: utf-8 -*-

"""
@File    : longestObstacleCourseAtEachPosition.py
@Author  : wenhao
@Time    : 2023/3/9 16:33
@LC      : 1964
"""
from typing import List
from bisect import bisect_right


class Solution:
    # 其实就是 300 题的相同情况
    # 二分 + 贪心
    # 对于每个元素 贪心地替代 二分找到的位置 这样保证了以每个数字结尾的递增序列最长
    def longestObstacleCourseAtEachPosition1(self, obstacles: List[int]) -> List[int]:
        n = len(obstacles)
        g = []
        ans = [0] * n
        for i, x in enumerate(obstacles):
            p = bisect_right(g, x)
            ans[i] = p + 1  # 这里 wa 了一次😒
            if p == len(g):
                g.append(x)
            else:
                g[p] = x
        return ans

    # 先写 dp TLE😂 我就知道没这么简单 那看来就是 二分+贪心了
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        n = len(obstacles)
        f = [0] * n
        for i in range(n):
            for j in range(i):
                if obstacles[j] <= obstacles[i]:
                    f[i] = max(f[i], f[j])
            f[i] += 1
        return f
