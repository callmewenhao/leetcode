# -*- coding: utf-8 -*-

"""
@File    : repairCars.py
@Author  : wenhao
@Time    : 2023/2/18 22:20
@LC      : 2569
"""
"""
lazy 线段树
问题 有一个数组
更新一个子数组的值（都加上一个数、把子数组内的元素取反，······）
查询一个子数组的值（求和，求最大/小值，······）

两大思想
1. 挑选 O(n) 个特殊区间，使得任意一个区间可以拆分为 O(log n) 个特殊区间 （用最近公共祖先来思考）
    O(n) <= 4n
挑选 O(n) 个特殊区间 build()

2. lazy 更新 / 延迟更新

lazy tag：用一个数组维护每个区间需要更新的值
如果这个值 = 0 表示不需要更新
如果这个值 != 0 表示更新操作在这个区间停住了 不继续递归更新子区间了

如果后面又来了一个更新 破坏了有 lazy tag 的区间 那么这个区间就得继续递归更新

"""
from typing import List


class Solution:
    def handleQuery(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:

        n = len(nums1)
        cnt1 = [0] * (4 * n)  # 统计区间中 1 的个数
        todo = [False] * (4 * n)  # lazy 数组

        def maintain(o: int) -> None:
            cnt1[o] = cnt1[o * 2] + cnt1[o * 2 + 1]

        def build(o: int, l: int, r: int) -> None:
            if l == r:
                # 操作
                cnt1[o] = nums1[l - 1]  # l 从 1 开始 故需要减 1
                return
            m = l + (r - l) // 2
            build(2 * o, l, m)
            build(2 * o + 1, m + 1, r)
            # 维护 额外的东西
            maintain(o)

        def do(o: int, l: int, r: int) -> None:
            cnt1[o] = r - l + 1 - cnt1[o]
            todo[o] = not todo[o]

        # 更新 [L, R]
        def update(o: int, l: int, r: int, L: int, R: int) -> None:
            if L <= l and r <= R:
                # 更新
                do(o, l, r)
                return

            m = l + (r - l) // 2

            # 需要继续递归 就把 to do [o] 的内容传下去（给左右儿子）
            if todo[o]:
                do(o * 2, l, m)
                do(o * 2 + 1, m + 1, r)
                todo[o] = False  # 清空

            if m >= L: update(o * 2, l, m, L, R)
            if m < R: update(o * 2 + 1, m + 1, r, L, R)
            # 维护
            maintain(o)

        build(1, 1, n)
        ans = []
        s = sum(nums2)
        for op, l, r in queries:
            if op == 1: update(1, 1, n, l + 1, r + 1)  # 前三个参数固定不变
            elif op == 2: s += l * cnt1[1]
            else: ans.append(s)
        return ans



