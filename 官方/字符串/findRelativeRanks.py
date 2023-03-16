# -*- coding: utf-8 -*-

"""
@File    : findRelativeRanks.py
@Author  : wenhao
@Time    : 2023/3/13 13:59
@LC      : 506
"""
from typing import List


class Solution:
    # 好多小细节没注意 😣
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        idx = [_ for _ in range(n)]
        score_idx = list(zip(score, idx))
        score_idx.sort(key=lambda x: x[0], reverse=True)

        # print(score_idx)
        ans = [''] * n
        for i, (_, idx) in enumerate(score_idx):
            if i == 0:
                ans[idx] = "Gold Medal"
            elif i == 1:
                ans[idx] = "Silver Medal"
            elif i == 2:
                ans[idx] = "Bronze Medal"
            else:
                ans[idx] = f"{i + 1}"
        return ans









