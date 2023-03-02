# -*- coding: utf-8 -*-

"""
@File    : T2.py
@Author  : wenhao
@Time    : 2023/2/18 22:20
@LC      : 2567
"""
from typing import List


class Solution:
    # 脑筋急转弯 😂
    # 要使得分最小 则修改后的数 不能使 最小得分 和 最大得分 变大
    # 显然 如果让 最小值等于剩余某个值 或者 最大值等于剩余某个值 会有最小得分=0 且缩小了最大得分
    # 问题就变成 在上述基础之上 再改一个数 使最大得分变小
    # 有两种选择 改剩余元素得最大值或最小值
    # 一共有 3 种情况
    # 排序
    # 改最小和最大
    # 改最小和次小
    # 改最大和次大
    def minimizeSum(self, nums: List[int]) -> int:
        nums.sort()
        a = nums[-1] - nums[2]
        b = nums[-3] - nums[0]
        c = nums[-2] - nums[1]
        return min(a, b, c)
