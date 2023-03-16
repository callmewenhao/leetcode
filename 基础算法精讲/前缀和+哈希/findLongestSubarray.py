# -*- coding: utf-8 -*-

"""
@File    : findLongestSubarray.py
@Author  : wenhao
@Time    : 2023/3/11 21:51
@LC      : 面试题 17.05
"""
from typing import List
from collections import Counter


class Solution:
    # 这个题目思路和之前做的统计 0 1 个数相同的子区间相同的思想
    # 字母对应 -len(ch) 数字对应 len(ch)
    # 问题转化成 找到一个和为 0 的最长子数组
    # 我们在寻找答案的过程中维护子数组起点和长度
    def findLongestSubarray(self, array: List[str]) -> List[str]:
        # 预处理
        n = len(array)
        pre = [0] * (n + 1)
        for i, ch in enumerate(array):
            if ch[0].isdigit():
                pre[i + 1] = 1 + pre[i]
            else:
                pre[i + 1] = -1 + pre[i]
        # 答案
        start = -1
        max_size = 0
        c = Counter({0: -1})  # 提前存入这个 0:-1 保证前缀子数组也能够被找到
        for i in range(1, n + 1):  # 遍历 i=1 之后的元素
            if pre[i] in c:  # c 中存在相同值
                if max_size < i - c[pre[i]]:  # 是否需要更新
                    max_size = i - c[pre[i]]  # 新长度
                    start = c[pre[i]] + 1  # 子数组不包含 c[pre[i]] 所以起点为 c[pre[i]] + 1
            else:
                c[pre[i]] = i - 1  # 在 c 中放的是真实的坐标 所以要把 i - 1 放入 c
        if max_size == 0:
            return []
        return array[start:start + max_size]
