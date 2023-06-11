# -*- coding: utf-8 -*-

"""
@File    : isValid.py
@Author  : wenhao
@Time    : 2023/5/3 15:44
@LC      : 1003
"""


class Solution:
    # 栈 模拟
    def isValid(self, s: str) -> bool:
        st = []
        for c in map(ord, s):
            if c > ord('a') and (len(st) == 0 or c - st.pop() != 1):
                return False
            if c < ord('c'):
                st.append(c)
        return len(st) == 0







