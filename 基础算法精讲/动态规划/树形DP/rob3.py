# -*- coding: utf-8 -*-

"""
@File    : rob3.py
@Author  : wenhao
@Time    : 2023/4/8 22:22
@LC      : 337
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from Tree import TreeNode
from typing import Optional
from functools import cache


class Solution:
    # 优化 树形DP 对于某个节点 选 或者 不选
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node is None:
                return 0, 0
            l_rob, l_not_rob = dfs(node.left)
            r_rob, r_not_rob = dfs(node.right)
            rob = node.val + l_not_rob + r_not_rob
            not_rob = max(l_rob, l_not_rob) + max(r_rob, r_not_rob)
            return rob, not_rob

        return max(dfs(root))

    # 第一次做法 类似状态机 DP
    def rob(self, root: Optional[TreeNode]) -> int:
        # dfs(node, can)  当前节点 能不能偷
        @cache
        def dfs(node: TreeNode, can: bool) -> int:
            if node is None:
                return 0
            if not can:
                return dfs(node.left, True) + dfs(node.right, True)
            res1 = dfs(node.left, True) + dfs(node.right, True)
            res2 = node.val + dfs(node.left, False) + dfs(node.right, False)
            return max(res1, res2)

        return max(dfs(root, True), dfs(root, False))
