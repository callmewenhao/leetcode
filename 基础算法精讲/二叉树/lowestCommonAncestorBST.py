# -*- coding: utf-8 -*-

"""
@File    : lowestCommonAncestorBST.py
@Author  : wenhao
@Time    : 2023/2/3 22:09
@LC      : 235
"""
from Tree import TreeNode


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        x = root.val
        if p.val < x and q.val < x:
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val > x and q.val > x:
            return self.lowestCommonAncestor(root.right, p, q)
        return root







