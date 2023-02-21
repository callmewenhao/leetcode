# -*- coding: utf-8 -*-

"""
@File    : balancedString.py
@Author  : wenhao
@Time    : 2023/2/13 9:26
@LC      : 1234
"""
from math import inf
from collections import Counter


class Solution:
    '''
    思路：
    同向双指针：
    '''
    def balancedString(self, s: str) -> int:
        cnt, m = Counter(s), len(s)
        if all(cnt[x] == m for x in "QWER"):
            return 0
        ans, left = inf, 0
        for right, c in enumerate(s):
            cnt[c] -= 1
            while all(cnt[x] <= m for x in "QWER"):
                ans = min(ans, right - left + 1)
                cnt[s[left]] += 1
                left += 1
        return ans
