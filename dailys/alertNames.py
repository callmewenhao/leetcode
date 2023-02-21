# -*- coding: utf-8 -*-

"""
@File    : alertNames.py
@Author  : wenhao
@Time    : 2023/2/7 18:33
@LC      : 1604
"""
from typing import List
from collections import defaultdict
from string import digits


class Solution:
    # optimize
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        d = defaultdict(list)
        for name, t in zip(keyName, keyTime):
            t = int(t[:2]) * 60 + int(t[3:])
            d[name].append(t)
        ans = []
        for name, ts in d.items():
            if (n := len(ts)) > 2:
                ts.sort()
                for i in range(n - 2):
                    if ts[i + 2] - ts[i] <= 60:
                        ans.append(name)
                        break
        ans.sort()
        return ans


    def alertNames1(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        d = defaultdict(list)
        for name, t in zip(keyName, keyTime):
            time = int(t[0]) * 1000 + int(t[1]) * 100 + int(t[3]) * 10 + int(t[4])
            d[name].append(time)

        ans = []
        for k, v in d.items():
            v.sort()
            for i in range(len(v) - 2):
                if v[i] + 100 >= v[i + 2]:
                    ans.append(k)
                    break
        return sorted(ans)

