# -*- coding: utf-8 -*-

"""
@File    : validateStackSequences.py
@Author  : wenhao
@Time    : 2023/2/16 17:02
@LC      : 
"""
from typing import List


class Solution:
    # 模拟入栈过程，如果栈顶等于当前出栈值，则出栈，最后返回 len(st) == 0
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        n = len(pushed)
        st = []

        i = 0
        for num in pushed:
            st.append(num)
            while st and i < n and st[-1] == popped[i]:
                st.pop()
                i += 1
        return len(st) == 0



















