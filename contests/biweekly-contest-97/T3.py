# -*- coding: utf-8 -*-

"""
@File    : beautifulSubarrays.py
@Author  : wenhao
@Time    : 2023/2/4 22:16
@LC      : 
"""

from typing import List
from collections import Counter

class Solution:
    def maximizeWin(self, prizePositions: List[int], k: int) -> int:
        ans = []
        cnt = 0
        left = 0

        for right, num in enumerate(prizePositions):
            bound = prizePositions[left] + k
            if num <= bound:
                cnt += 1
            else:
                ans.append(cnt)
                cnt = 1
                left = right

        ans.append(cnt)
        ans.sort(reverse=True)
        return ans[0] + ans[1] if len(ans) > 1 else ans[0]
