# -*- coding: utf-8 -*-

"""
@File    : expressiveWords.py
@Author  : wenhao
@Time    : 2023/2/1 21:26
@LC      : 809
"""
from typing import  List

class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:

        l1 = []
        frag = ""
        for i, c in enumerate(s):
            if i == 0:
                frag = s[0]
            else:
                if s[i] == s[i - 1]:
                    frag += s[i]
                else:
                    l1.append(frag)
                    frag = s[i]
        l1.append(frag)

        ans = 0
        for word in words:
            idx = 0
            for i, c in enumerate(word):
                if i == 0:
                    frag = word[0]
                else:
                    if word[i] == word[i - 1]:
                        frag += s[i]
                    else:
                        if l1[idx][0] != frag[0] or len(l1[idx]) < len(frag) or len(frag) < len(l1[idx]) <= 2:
                            break
                        frag = s[i]
            if l1[idx][0] != frag[0] or len(l1[idx]) < len(frag) or len(frag) < len(l1[idx]) <= 2:
                continue
            ans += 1

        return ans


