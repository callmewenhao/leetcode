# -*- coding: utf-8 -*-

"""
@File    : 1170numSmallerByFrequency.py
@Author  : wenhao
@Time    : 2023/6/10 10:22
@LC      : 1170
"""
from typing import List
from collections import Counter


class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        n = len(queries)
        dict = [0] * n
        for i, query, in enumerate(queries):
            query = list(sorted(list(query)))
            cnt = Counter(query)
            dict[i] = cnt[query[0]]

        ans = [0] * n
        for i, word in enumerate(words):
            word = list(sorted(list(word)))
            cnt = Counter(word)
            for j in range(n):
                if cnt[word[0]] > dict[j]:
                    ans[j] += 1

        return ans

