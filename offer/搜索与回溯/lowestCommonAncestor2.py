# -*- coding: utf-8 -*-

"""
@File    : lowestCommonAncestor2.py
@Author  : wenhao
@Time    : 2023/2/7 20:19
@LC      : 
"""
from Tree import TreeNode


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root is None:
            return None
        if root.val == p.val or root.val == q.val:
            return root

        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)

        if l is None:
            return r
        if r is None:
            return l
        return root



