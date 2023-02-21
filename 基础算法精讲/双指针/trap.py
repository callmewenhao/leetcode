# -*- coding: utf-8 -*-

"""
@File    : trap.py
@Author  : wenhao
@Time    : 2023/1/29 23:03
"""
from typing import List


class Solution:
    # 使用双指针优化空间复杂度
    def trap(self, height: List[int]) -> int:
        n = len(height)
        pre_max = suf_max = 0

        ans = 0
        l, r = 0, n - 1
        while l <= r:  # 可以不用等于
            pre_max = max(pre_max, height[l])
            suf_max = max(suf_max, height[r])
            if pre_max < suf_max:
                ans += pre_max - height[l]
                l += 1
            else:
                ans += suf_max - height[r]
                r -= 1
        return ans

    # 使用前缀最大值 后缀最大值
    def trap1(self, height: List[int]) -> int:
        n = len(height)
        pre_max = [height[0]] * n
        for i in range(1, n):
            pre_max[i] = max(pre_max[i - 1], height[i])

        suf_max = [height[-1]] * n
        for i in range(n - 2, -1, -1):
            suf_max[i] = max(suf_max[i + 1], height[i])

        ans = 0
        for h, p, s in zip(height, pre_max, suf_max):
            ans += min(p, s) - h
        return ans
