# -*- coding: utf-8 -*-

"""
@File    : shortestAlternatingPaths.py
@Author  : wenhao
@Time    : 2023/2/2 10:35
@LC      : 1129
"""
from typing import List


class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red_path = [set() for _ in range(n)]
        blue_path = [set() for _ in range(n)]
        dist = [[None, None] for _ in range(n)]
        dist[0] = [0, 0]

        step = 0
        now_red = [0]
        now_blue = [0]

        # build two graph
        for start, end in redEdges:
            red_path[start].add(end)
        for start, end in blueEdges:
            blue_path[start].add(end)

        # step 1 找到分别以红边开始和以蓝边开始的两条最短路径
        while len(now_red) != 0 or len(now_blue) != 0:
            new_red, new_blue = [], []
            step += 1
            if len(now_blue) != 0:
                for point in now_blue:
                    for next_point in red_path[point]:
                        if dist[next_point][0] is None:
                            new_red.append(next_point)
                            dist[next_point][0] = step
            if len(now_red) != 0:
                for point in now_red:
                    for next_point in blue_path[point]:
                        if dist[next_point][1] is None:
                            new_blue.append(next_point)
                            dist[next_point][1] = step
            now_red, now_blue = new_red, new_blue

        # step 2 在这两条最短路径中选择小的，merge成我们的答案
        ans = []
        for i in range(n):
            if dist[i][0] is None and dist[i][1] is None:
                ans.append(-1)
            elif dist[i][0] is not None and dist[i][1] is not None:
                ans.append(min(dist[i][0], dist[i][1]))
            elif dist[i][0] is not None:
                ans.append(dist[i][0])
            else:
                ans.append(dist[i][1])
        return ans
