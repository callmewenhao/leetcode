# -*- coding: utf-8 -*-

"""
@File    : T2.py
@Author  : wenhao
@Time    : 2023/4/22 14:49
@LC      : 
"""
from typing import List
from collections import Counter


class Solution:
    def adventureCamp(self, expeditions: List[str]) -> int:
        ans = 0
        mx = 0
        cnt = Counter(expeditions[0].split("->"))  # init

        for i in range(1, len(expeditions)):
            ps = expeditions[i].split("->")
            t = 0
            for p in ps:
                if p and p not in cnt:
                    t += 1
                    cnt[p] += 1
            if t > mx:
                ans = i
                mx = t

        return ans if ans > 0 else -1
