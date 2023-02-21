# -*- coding: utf-8 -*-

"""
@File    : generateParenthesis.py
@Author  : wenhao
@Time    : 2023/1/31 23:09
@LC      : 
"""
from typing import List


class Solution:
    # 灵神 枚举选哪个
    def generateParenthesis(self, n: int) -> List[str]:
        m = n * 2
        ans = []
        path = [''] * m

        def dfs(i: int, open: int):
            if i == m:
                ans.append(''.join(path))
                return
            if open < n:
                path[i] = "("
                dfs(i + 1, open + 1)
            if i - open < open:
                path[i] = ")"
                dfs(i + 1, open)

        dfs(0, 0)
        return ans

    # 选与不选
    def generateParenthesis1(self, n: int) -> List[str]:
        ans = []
        path = []

        def dfs(l: int, r: int):
            if l < 0 or r < 0:
                return
            if l == 0 and r == 0:
                ans.append(''.join(path))
                return
            # 放左括号
            path.append('(')
            dfs(l - 1, r)
            path.pop()
            # 能不能放右括号
            if l < r:
                path.append(')')
                dfs(l, r - 1)
                path.pop()
        dfs(n, n)
        return ans
