# -*- coding: utf-8 -*-

"""
@File    : T2.py
@Author  : wenhao
@Time    : 2023/2/26 9:45
@LC      : 
"""
from typing import List


class Solution:
    # 和🐏佬的思路基本一致
    # 遍历一边 维护一个 前缀模m 即可
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        mod = 0
        ans = []
        for ch in word:
            mod = (mod * 10 + int(ch)) % m
            if mod == 0:
                ans.append(1)
            else:
                ans.append(0)
        return ans
