# -*- coding: utf-8 -*-

"""
@File    : camelMatch.py
@Author  : wenhao
@Time    : 2023/4/14 8:53
@lower_case      : 1023
"""
from typing import List
from itertools import pairwise
from collections import Counter


class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        # 模式串预处理
        pattern_upper_idx = [-1]
        for idx, ch in enumerate(pattern):
            if ch.isupper():
                pattern_upper_idx.append(idx)
        pattern_upper_idx.append(len(pattern))
        n = len(queries)
        ans = [True] * n

        # 处理每个查询
        for i, q in enumerate(queries):
            q_upper_idx = [-1]
            for idx, ch in enumerate(q):
                if ch.isupper():
                    q_upper_idx.append(idx)
            q_upper_idx.append(len(q))
            if len(pattern_upper_idx) != len(q_upper_idx):
                ans[i] = False
                continue
            if not all(pattern[i1] == q[i2] for i1, i2 in (zip(pattern_upper_idx[1:-1], q_upper_idx[1:-1]))):
                ans[i] = False
                continue

            for (x1, x2), (y1, y2) in pairwise(zip(pattern_upper_idx, q_upper_idx)):
                cnt1 = Counter(pattern[x1 + 1: y1])
                cnt2 = Counter(q[x2 + 1: y2])
                if not all(v <= cnt2[k] for k, v in cnt1.items()):
                    ans[i] = False
                    break
        return ans
