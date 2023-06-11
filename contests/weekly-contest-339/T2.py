# -*- coding: utf-8 -*-

"""
@File    : T2.py
@Author  : wenhao
@Time    : 2023/4/2 10:29
@LC      : 
"""
from typing import List
from collections import Counter


class Solution:
    # 优化
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        ans = []
        cnt = Counter(nums)

        while cnt:
            row = list(cnt)  # 取出 cnt 中的 key
            ans.append(row)
            for num in row:
                cnt[num] -= 1
                if cnt[num] == 0:
                    del cnt[num]  # 从 cnt 中删除 num
        return ans

    # 排序 + vis 数组思路
    def findMatrix1(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        vis = [False] * n
        cnt = n

        ans = []
        while cnt:
            i = 0
            res = []

            for idx, b in enumerate(vis):
                if not b:
                    i = idx
            res.append(nums[i])
            vis[i] = True
            cnt -= 1

            for j in range(i + 1, n):
                if not vis[j] and res[-1] < nums[j]:
                    res.append(nums[j])
                    vis[j] = True
                    cnt -= 1
            ans.append(res)
        return ans
