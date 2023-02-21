# -*- coding: utf-8 -*-

"""
@File    : robotWithString.py
@Author  : wenhao
@Time    : 2023/1/6 22:36
"""
from collections import Counter
from string import ascii_lowercase

class Solution:
    def robotWithString(self, s: str) -> str:
        ans = []
        cnt = Counter(s)
        min_ch = 0
        st = []
        for c in s:
            cnt[c] -= 1
            while min_ch < 25 and cnt[ascii_lowercase[min_ch]] == 0:
                min_ch += 1
            st.append(c)
            while st and st[-1] <= ascii_lowercase[min_ch]:
                ans.append(st.pop())
        return "".join(ans)

