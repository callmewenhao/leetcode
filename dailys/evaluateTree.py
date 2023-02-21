# -*- coding: utf-8 -*-

"""
@File    : evaluateTree.py
@Author  : wenhao
@Time    : 2023/2/7 20:01
@LC      : 2331
"""
from Tree import TreeNode
from typing import Optional


class Solution:
    # optimize 自身递归
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if root.left is None and root.right is None:
            return root.val == 1
        l = self.evaluateTree(root.left)
        r = self.evaluateTree(root.right)
        if root.val == 2:
            return l or r
        return l and r

    def evaluateTree1(self, root: Optional[TreeNode]) -> bool:

        def dfs(root: TreeNode) -> bool:
            if root.left is None and root.right is None:
                return root.val == 1
            l = dfs(root.left)
            r = dfs(root.right)
            if root.val == 2:
                return l or r
            return l and r

        return dfs(root)
