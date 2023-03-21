# -*- coding: utf-8 -*-

"""
@File    : repairCars.py
@Author  : wenhao
@Time    : 2023/3/19 11:26
@LC      : 
"""
from typing import List
from collections import Counter


class Solution:
    # 同余分组 典中典 😂
    # 优化
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        cnt = Counter(num % value for num in nums)  # 统计余数个数
        ans = 0
        while cnt[ans % value]:
            cnt[ans % value] -= 1
            ans += 1
        return ans

    def findSmallestInteger1(self, nums: List[int], value: int) -> int:
        arr = [num % value for num in nums]
        cnt = Counter()
        for mod in arr:
            cnt[mod] += 1
        ans = 0
        while True:
            mod = ans % value
            if cnt[mod] <= 0:
                return ans
            cnt[mod] -= 1
            ans += 1
