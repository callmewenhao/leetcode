# -*- coding: utf-8 -*-

"""
@File    : findMaxLength.py
@Author  : wenhao
@Time    : 2023/3/10 15:48
@LC      : 525
"""
from typing import List
from collections import Counter


class Solution:
    # 还是要对题目进行转化 😂
    def findMaxLength(self, nums: List[int]) -> int:
        # 预处理
        n = len(nums)
        pre = [0] * (n + 1)
        for i, num in enumerate(nums):
            if num == 1:
                pre[i + 1] = pre[i] + 1
            else:
                pre[i + 1] = pre[i] - 1

        # 寻找答案
        ans = 0
        c = Counter()
        for i, x in enumerate(pre):
            if x in c:
                ans = max(ans, i - c[x])
            else:
                c[x] = i  # 还是贪心思想 存储最小下标
        return ans
