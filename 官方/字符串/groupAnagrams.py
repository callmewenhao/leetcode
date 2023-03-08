# -*- coding: utf-8 -*-

"""
@File    : groupAnagrams.py
@Author  : wenhao
@Time    : 2023/3/7 21:52
@LC      : 49
"""
from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for word in strs:
            k = ''.join(sorted(word))
            d[k].append(word)
        return list(d.values())








