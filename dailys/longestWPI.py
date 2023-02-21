# -*- coding: utf-8 -*-

"""
@File    : longestWPI.py
@Author  : wenhao
@Time    : 2023/2/14 9:59
@LC      : 1124
"""
from typing import List
from itertools import accumulate

class Solution:
    # 抄灵神代码
    def longestWPI(self, hours: List[int]) -> int:
        n = len(hours)
        s = [0] * (n + 1)
        st = [0]  # 单调栈的栈底必为0
        for j, h in enumerate(hours, 1):
            s[j] = s[j - 1] + (1 if h > 8 else -1)
            if s[j] < s[st[-1]]:
                st.append(j)
        ans = 0
        for i in range(n, 0, -1):
            while st and s[i] > s[st[-1]]:
                ans = max(ans, i - st.pop())
        return ans


    # 看灵神题解写代码
    def longestWPI1(self, hours: List[int]) -> int:
        n = len(hours)
        nums = [0] * n
        for i, h in enumerate(hours):
            nums[i] = 1 if h > 8 else -1
        # prefix sum
        pre_sum = list(accumulate(nums, initial=0))
        # 找到所有可能的左端点，存放在单调栈中
        st = []
        for i, v in enumerate(pre_sum):
            if len(st) == 0:
                st.append(i)
                continue
            if v < pre_sum[st[-1]]:
                st.append(i)
        # 计算答案
        ans = 0
        i = len(pre_sum) - 1
        while len(st):
            while 0 <= i and pre_sum[st[-1]] >= pre_sum[i]:
                i -= 1
            ans = max(ans, i - st[-1])
            st.pop()
        return ans



