# -*- coding: utf-8 -*-

"""
@File    : maxDepth.py
@Author  : wenhao
@Time    : 2023/2/4 16:48
@LC      : 
"""
from Tree import TreeNode

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
