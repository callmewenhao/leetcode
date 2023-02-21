# -*- coding: utf-8 -*-

"""
@File    : lowestCommonAncestor.py
@Author  : wenhao
@Time    : 2023/2/7 20:13
@LC      : 
"""
from Tree import TreeNode


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root







