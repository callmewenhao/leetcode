# -*- coding: utf-8 -*-

"""
@File    : minDepth.py
@Author  : wenhao
@Time    : 2023/2/3 16:00
@LC      : 111
"""
from typing import Optional
from Tree import TreeNode

class Solution:
    # bfs 找第一个叶子节点

    # dfs
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        l = self.minDepth(root.left)
        r = self.minDepth(root.right)

        if l == 0:
            return r + 1
        if r == 0:
            return l + 1
        return min(r, l) + 1