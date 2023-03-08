# -*- coding: utf-8 -*-

"""
@File    : longestCommonPrefix.py
@Author  : wenhao
@Time    : 2023/3/7 9:47
@LC      : 14
"""
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        mi = min(len(word) for word in strs)

        ans = ""
        for i in range(mi):
            c = strs[0][i]
            for j in range(1, len(strs)):
                if strs[j][i] != c:
                    return ans  # 提前返回
            ans += c
        return ans  # 都相同时




