# -*- coding: utf-8 -*-

"""
@File    : 1110delNodes.py
@Author  : wenhao
@Time    : 2023/5/30 8:56
@LC      : 1110
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from Tree import TreeNode
from typing import Optional, List


class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        s = set(to_delete)

        ans = []
        if root.val not in s:
            ans.append(root)

        # 添加产生的新树
        def dfs(x: TreeNode, fa: TreeNode, d):
            if x is None:
                return

            if x.left:
                dfs(x.left, x, 0)
            if x.right:
                dfs(x.right, x, 1)
            if x.val in s:
                if x.left:
                    ans.append(x.left)
                    x.left = None
                if x.right:
                    ans.append(x.right)
                    x.right = None
                if fa and d == 0:
                    fa.left = None
                if fa and d == 1:
                    fa.right = None
        dfs(root, None, 0)
        return ans
