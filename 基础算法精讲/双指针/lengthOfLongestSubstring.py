# -*- coding: utf-8 -*-

"""
@File    : lengthOfLongestSubstring.py
@Author  : wenhao
@Time    : 2023/4/12 21:06
@LC      : 3
"""
class Solution:


    # 同向双指针 滑动窗口
    def lengthOfLongestSubstring(self, s: str) -> int:
        cnt = [0] * 128  # hash biao
        l = ans = 0
        for r, ch in enumerate(s):
            cnt[ord(ch)] += 1
            while cnt[ord(ch)] > 1:
                cnt[ord(s[l])] -= 1
                l += 1
            ans = max(ans, r - l + 1)
        return ans
