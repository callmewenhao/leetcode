# -*- coding: utf-8 -*-

"""
@File    : isBalanced.py
@Author  : wenhao
@Time    : 2023/2/4 16:49
@LC      : 
"""
from Tree import TreeNode


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True

        def get_height(root: TreeNode):
            if root is None:
                return 0
            l = get_height(root.left)
            r = get_height(root.right)
            if l == -1 or r == -1 or abs(l - r) > 1:
                return -1
            return max(l, r) + 1

        return get_height(root) != -1
