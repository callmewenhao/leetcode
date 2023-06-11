# -*- coding: utf-8 -*-

"""
@File    : 1080sufficientSubset.py
@Author  : wenhao
@Time    : 2023/5/22 9:21
@LC      : 1080
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
from Tree import TreeNode


class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        def dfs(node: Optional[TreeNode], left: int) -> bool:
            if node is None:
                return 0 >= left

            res1 = dfs(node.left, left - node.val)
            res2 = dfs(node.right, left - node.val)

            res = res1 or res2
            if node.left and not node.right:
                res = res1
            if not node.left and node.right:
                res = res2

            if not res1:
                node.left = None
            if not res2:
                node.right = None

            return res

        ans = dfs(root, limit)
        if not ans: return None
        return root
