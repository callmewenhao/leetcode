# -*- coding: utf-8 -*-

"""
@File    : isSymmetric.py
@Author  : wenhao
@Time    : 2023/2/3 14:21
@LC      : 101
"""
from typing import Optional
from Tree import TreeNode


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(n1: TreeNode, n2: TreeNode) -> bool:
            if n1 is None or n2 is None:
                return n1 == n2
            return n1.val == n2.val and \
                   dfs(n1.left, n2.right) and \
                   dfs(n1.right, n2.left)
        return dfs(root, root)  # trick 传入相同的两棵树

