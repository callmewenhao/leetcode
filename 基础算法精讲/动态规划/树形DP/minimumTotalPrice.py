# -*- coding: utf-8 -*-

"""
@File    : minimumTotalPrice.py
@Author  : wenhao
@Time    : 2023/4/17 19:19
@LC      : 
"""

"""
树形 DP   
也叫树上最大独立集

总体思路与 rob3 类似
x, y
x 选： += y 不选
x 不选： += max(y 选, y 不选)

# 1. 首先记录 每个点经过的次数
# 2. 写一个树形 DP
"""
from typing import List


class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        # 建树
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        cnt = [0] * n  # 每个节点在路径上的经过次数  不经过的点是 0 这样就不会受影响了
        for start, end in trips:
            # 找路径 找到终点就返回 true
            # 遍历一棵树：传入当前节点 + 父节点 防止回头（不使用 vis）
            def dfs(x: int, fa: int) -> bool:
                if x == end:
                    cnt[x] += 1
                    return True
                for y in g[x]:
                    if y != fa and dfs(y, x):
                        cnt[x] += 1  # 说明当前节点在路径上
                        return True
                return False
            dfs(start, -1)
        # 写一个类似打家劫舍3的DP
        # 返回 (x 减半时的子树最小总和，x 不减半时的子树最小总和)
        def dfs(x: int, fa: int) -> (int, int):
            not_have = price[x] * cnt[x]
            have = not_have // 2
            for y in g[x]:
                if y != fa:
                    nh, h = dfs(y, x)
                    not_have += min(nh, h)
                    have += nh
            return not_have, have
        return min(dfs(0, -1))












