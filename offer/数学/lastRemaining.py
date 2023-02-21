# -*- coding: utf-8 -*-

"""
@File    : lastRemaining.py
@Author  : wenhao
@Time    : 2023/2/10 22:46
@LC      : 
"""


class Solution:
    # 约瑟夫环，暴力枚举会超时 😢
    # 数学解法：从最后一个剩余的人开始倒推，倒推 n - 1 轮
    def lastRemaining(self, n: int, m: int) -> int:
        ans = 0  # 最后剩下的人坐标必为0
        # 开始倒推
        for i in range(2, n + 1):
            ans = (ans + m) % i  # 公式：上一轮坐标 = （当前坐标 + m）% 上一轮长度
        return ans
