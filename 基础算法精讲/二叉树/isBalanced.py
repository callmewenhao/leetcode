# -*- coding: utf-8 -*-

"""
@File    : isBalanced.py
@Author  : wenhao
@Time    : 2023/2/3 14:29
@LC      : 110
"""
from typing import Optional
from Tree import TreeNode


class Solution:
    # optimize
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def get_height(root):
            if root is None:
                return 0
            l_h = get_height(root.left)
            if l_h == -1:
                return -1
            r_h = get_height(root.right)
            if r_h == -1 or abs(l_h - r_h) > 1:
                return -1
            return max(l_h, r_h) + 1
        return get_height(root) != -1


    # 求深度
    # def maxDepth(self, root: Optional[TreeNode]) -> int:
    #     if root is None:
    #         return 0
    #     return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
    #
    # def isBalanced(self, root: Optional[TreeNode]) -> bool:
    #     if root is None:
    #         return True
    #     return self.isBalanced(root.left) and \
    #            self.isBalanced(root.right) and \
    #            abs(self.maxDepth(root.left) - self.maxDepth(root.right)) <= 1
