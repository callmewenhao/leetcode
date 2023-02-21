# -*- coding: utf-8 -*-

"""
@File    : invertTree.py
@Author  : wenhao
@Time    : 2023/2/3 15:58
@LC      : 226
"""
from typing import Optional
from Tree import TreeNode


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        l = self.invertTree(root.left)
        r = self.invertTree(root.right)
        root.left = r
        root.right = l
        return root
