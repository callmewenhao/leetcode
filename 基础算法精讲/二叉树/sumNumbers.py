# -*- coding: utf-8 -*-

"""
@File    : sumNumbers.py
@Author  : wenhao
@Time    : 2023/2/3 16:07
@LC      : 129
"""
from typing import Optional
from Tree import TreeNode


class Solution:
    # optimize
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, s):
            if node is None:
                return 0
            s = s * 10 + node.val
            if node.left is None and node.right is None:
                return s
            return dfs(node.left, s) + dfs(node.right, s)
        return dfs(root, 0)

    def sumNumbers1(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(node, s):
            if node is None:
                return
            s = s * 10 + node.val
            if node.left is None and node.right is None:
                nonlocal ans
                ans += s
                return
            dfs(node.left, s)
            dfs(node.right, s)
        dfs(root, 0)
        return ans
