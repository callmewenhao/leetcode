# -*- coding: utf-8 -*-

"""
@File    : checkArithmeticSubarrays.py
@Author  : wenhao
@Time    : 2023/3/23 17:06
@LC      : 1630
"""
from typing import List
from collections import Counter


class Solution:
    # 分类讨论 暴力枚举 🤣
    # 其实就是多用几个循环判断 数组是否是 等差数列
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = [False] * len(l)  # 初始化答案
        cnt = Counter()  # 计数器判重
        for i, (left, right) in enumerate(zip(l, r)):
            cnt.clear()  # 计数器清空
            mx = max(nums[left: right + 1])  # 最大值
            mi = min(nums[left: right + 1])  # 最小值
            if (mx - mi) % (right - left) != 0:  # 步长不是整数
                ans[i] = False
                continue
            d = (mx - mi) // (right - left)
            if d == 0:  # 步长为零时
                ans[i] = True if all(num == nums[left] for num in nums[left: right + 1]) else False
                continue
            for num in nums[left: right + 1]:  # 遍历一边
                # 如果遇到 无法整除 或者 重复的值时 就不是等差数列
                if (num - mi) % d and cnt[(num - mi) // d] > 0:
                    ans[i] = False
                    break
                cnt[(num - mi) // d] += 1
                ans[i] = True
        return ans
