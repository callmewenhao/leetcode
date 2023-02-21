# -*- coding: utf-8 -*-

"""
@File    : maxSlidingWindow.py
@Author  : wenhao
@Time    : 2023/2/16 19:32
@LC      : 
"""

from typing import List
from collections import deque


class Solution:
    # 单纯求区间的最值——使用优先队列
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        mx = nums[0]
        q = deque()
        for i in range(k):
            while q and nums[q[-1]] <= nums[i]:
                q.pop()
            q.append(i)
            if mx < nums[i]:
                mx = nums[i]
        #
        ans = [mx]
        for i in range(k, len(nums)):
            while q and nums[q[-1]] <= nums[i]:
                q.pop()
            q.append(i)
            while q and q[0] <= i - k:
                q.popleft()
            ans.append(nums[q[0]])
        return ans











