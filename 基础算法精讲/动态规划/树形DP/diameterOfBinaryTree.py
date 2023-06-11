# -*- coding: utf-8 -*-

"""
@File    : diameterOfBinaryTree.py
@Author  : wenhao
@Time    : 2023/4/17 22:52
@LC      : 543
"""
from Tree import TreeNode
from typing import List, Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(node: TreeNode) -> int:
            if node is None:
                return -1
            l_len = dfs(node.left)
            r_len = dfs(node.right)
            nonlocal ans
            ans = max(ans, 2 + l_len + r_len)
            return max(l_len, r_len) + 1
        dfs(root)
        return ans

