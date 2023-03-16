# -*- coding: utf-8 -*-

"""
@File    : minNumberOfHours.py
@Author  : wenhao
@Time    : 2023/3/13 13:07
@LC      : 2383
"""
from typing import List


class Solution:
    # 其实就是简单模拟题目
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int],
                         experience: List[int]) -> int:
        ans = 0
        s1 = sum(energy)
        ans += max(s1 - initialEnergy + 1, 0)  # 被这里坑了😒

        s2 = initialExperience
        for e in experience:
            if s2 <= e:
                ans += e - s2 + 1
                s2 += 2 * e - s2 + 1  # 这里没想清楚 😣
            else:
                s2 += e

        return ans
