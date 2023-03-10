# -*- coding: utf-8 -*-

"""
@File    : minSubarray.py
@Author  : wenhao
@Time    : 2023/3/10 13:49
@LC      : 1590
"""
from typing import List
from itertools import accumulate
from collections import Counter


class Solution:
    # 不一起看星星 星星它亮有什么用
    # 我的思路 😂 第一遍有很多地方没想明白
    # 也是在 同余定理的基础上进行左右移项 下面是灵神的移项思路来修改我的代码
    # 注意 l r 是从 0 到 n 的 0表示空数组
    # (sum(l, r] - s) % p == 0 ==> (pre[r] - pre[l] - s) % p == 0
    # ==> ((pre[r] - s) - pre[l]) % p == 0 ==> (pre[r] - s) % p = pre[l] % p
    # 此时 答案区间长度是 r - l
    def minSubarray(self, nums: List[int], p: int) -> int:
        pre = list(accumulate(nums, initial=0))  # 前缀和可以使用一个变量优化掉
        s = pre[-1]
        # if s % p == 0:  # 这段代码可以被优化掉
        #     return 0

        ans = n = len(nums)
        last = {}
        for i, x in enumerate(pre):
            last[x % p] = i  # 先放进去再查询 可以保证空字串情况
            j = last.get((x - s) % p, -n)
            ans = min(ans, i - j)
        return ans if ans < n else -1

    def minSubarray1(self, nums: List[int], p: int) -> int:
        pre = 0  # 前缀和可以使用一个变量优化掉
        s = sum(nums)
        ans = n = len(nums)
        last = {0: -1}
        for i in range(n):
            pre += nums[i]
            last[pre % p] = i  # 先放进去再查询 可以保证空字串情况
            j = last.get((pre - s) % p, -n)
            ans = min(ans, i - j)

        return ans if ans < n else -1
