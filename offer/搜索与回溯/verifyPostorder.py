# -*- coding: utf-8 -*-

"""
@File    : verifyPostorder.py
@Author  : wenhao
@Time    : 2023/2/8 10:38
@LC      : 
"""
from typing import List


class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        def dfs(l, r) -> bool:
            if l >= r:
                return True

            root = postorder[r]
            m = l
            for i in range(l, r):
                if postorder[i] < root:
                    m += 1

            for i in range(m, r):
                if postorder[i] <= root:
                    return False

            return dfs(l, m - 1) and dfs(m, r - 1)

        n = len(postorder)
        return dfs(0, n - 1)
