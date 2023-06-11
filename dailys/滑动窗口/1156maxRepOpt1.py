# -*- coding: utf-8 -*-

"""
@File    : 1156maxRepOpt1.py
@Author  : wenhao
@Time    : 2023/6/3 16:11
@LC      : 1156
"""
from collections import Counter


class Solution:
    def maxRepOpt1(self, text: str) -> int:
        n = len(text)
        cnt = Counter(text)

        i = ans = 0
        while i < n:
            # 找一个连续区间
            j = i + 1
            while j < n and text[j] == text[i]:
                j += 1
            cnt_cur = j - i
            # ans = max(ans, cnt_cur)

            # 如果左右有空位
            if cnt_cur < cnt[text[i]] and (0 < i or j < n):
                ans = max(cnt_cur + 1, ans)

            # 每次 看看后面能否拼起来
            k = j + 1
            while k < n and text[k] == text[i]:
                k += 1
            ans = max(ans, min(k - i, cnt[text[i]]))
            i = j
        return ans
