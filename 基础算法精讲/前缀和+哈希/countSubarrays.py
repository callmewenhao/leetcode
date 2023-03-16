# -*- coding: utf-8 -*-

"""
@File    : countSubarrays.py
@Author  : wenhao
@Time    : 2023/3/16 9:35
@LC      : 2488
"""
from typing import List
from collections import Counter


class Solution:
    # 做过一遍还是没思路 🤣
    # 思路
    # 把数字分成 大于k 小于k
    # 然后分别计算左右两侧的数字数目
    # 左侧小于-左侧大于=右侧大于-右侧小于
    #
    # 两种做法
    # 1 统计左侧数字情况 然后遍历右端点 计算答案 或者
    # 2 统计右侧数字情况 然后遍历左端点 计算答案

    def countSubarrays(self, nums: List[int], k: int) -> int:
        pos = nums.index(k)
        cnt, x = Counter({0: 1}), 0
        for i in range(pos + 1, len(nums)):
            x += 1 if nums[i] > k else -1  #
            cnt[x] += 1

        ans, x = cnt[0] + cnt[1], 0
        for i in range(pos - 1, -1, -1):
            x += 1 if nums[i] < k else -1  #
            ans += cnt[x] + cnt[x + 1]
        return ans



    def countSubarrays1(self, nums: List[int], k: int) -> int:
        pos = nums.index(k)
        cnt, x = Counter({0: 1}), 0
        for i in range(pos - 1, -1, -1):
            x += 1 if nums[i] < k else -1  # 左侧小于为 1 大于为 -1
            cnt[x] += 1

        ans, x = cnt[0] + cnt[-1], 0
        for i in range(pos + 1, len(nums), 1):
            x += 1 if nums[i] > k else -1  # 右侧大于为 1 小于为 -1
            ans += cnt[x] + cnt[x - 1]
        return ans
