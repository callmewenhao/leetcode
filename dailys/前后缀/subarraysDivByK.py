# -*- coding: utf-8 -*-

"""
@File    : subarraysDivByK.py
@Author  : wenhao
@Time    : 2023/3/10 9:41
@LC      : 974
"""
from typing import List
from collections import Counter
from itertools import accumulate


class Solution:
    # 同余定理 😁
    # 如果 a % m == b % m 则 (a - b) % m == 0
    # 遍历前缀和数组 对于每个右边界 在哈希表中寻找合适的左端点 a % m == b % m 😁
    # 然后在更新 哈希表
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        pre = accumulate(nums, initial=0)
        cnt = Counter()

        ans = 0
        for x in pre:
            m = x % k
            if m in cnt:
                ans += cnt[m]
            cnt[m] += 1
        return ans
