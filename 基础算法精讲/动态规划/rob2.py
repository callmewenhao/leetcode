# -*- coding: utf-8 -*-

"""
@File    : rob2.py
@Author  : wenhao
@Time    : 2023/2/10 10:50
@LC      : 213
"""
from typing import List


class Solution:
    '''
    思路：
    分成：选第一间不选最后一间、选最后一间不选第一间两种情况讨论
    每种情况都是 DP ✌
    '''
    def rob(self, nums: List[int]) -> int:
        # 偷第一间房屋的最大值
        n = len(nums)
        if n == 1:  # 处理长度为 1 时的特殊情况，因为此时按下面的逻辑相当于啥也没选
            return nums[0]
        f0 = f1 = 0
        for i in range(n - 1):
            f0, f1 = f1, max(f1, f0 + nums[i])
        ans = f1
        # 不偷第一间房屋的最大值
        f0 = f1 = 0
        for i in range(1, n):
            f0, f1 = f1, max(f1, f0 + nums[i])
        ans = max(ans, f1)
        return ans
