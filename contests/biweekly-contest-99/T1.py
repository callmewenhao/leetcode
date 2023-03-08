# -*- coding: utf-8 -*-

"""
@File    : T1.py
@Author  : wenhao
@Time    : 2023/3/4 22:20
@LC      : 
"""
from typing import List


class Solution:
    # 贪心 小的数字放到前面
    # sort 然后分配数字
    # 奇数下标一个数 偶数下标一个数
    def splitNum1(self, num: int) -> int:
        # py 写法
        s = sorted(str(num))  # 直接对 字符 排序
        return int(''.join(s[::2])) + int(''.join(s[1::2]))

    # 比赛时做法
    def splitNum(self, num: int) -> int:
        nums = []
        while num:
            nums.append(num % 10)
            num /= 10
        nums.sort()

        num1 = num2 = 0

        for i in range(len(nums)):
            if (i & 1) == 0:
                num1 = 10 * num1 + nums[i]
            else:
                num2 = 10 * num2 + nums[i]
        return num1 + num2
