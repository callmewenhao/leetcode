# -*- coding: utf-8 -*-

"""
@File    : 1090largestValsFromLabels.py
@Author  : wenhao
@Time    : 2023/5/23 9:31
@LC      : 1090
"""
from typing import List
from collections import defaultdict, Counter


class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        values_and_labels = sorted(zip(values, labels), key=lambda p: -p[0])

        ans = idx = 0
        cnt = Counter()
        while numWanted > 0 and idx < len(values_and_labels):
            val = values_and_labels[idx][0]
            lab = values_and_labels[idx][1]
            if cnt[lab] < useLimit:
                ans += val
                cnt[lab] += 1
                numWanted -= 1
            idx += 1
        return ans
