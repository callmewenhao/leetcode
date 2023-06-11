# -*- coding: utf-8 -*-

"""
@File    : maxPathSum.py
@Author  : wenhao
@Time    : 2023/4/17 22:57
@LC      : 124
"""
from typing import List, Optional
from math import inf
from Tree import TreeNode
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 与 543 思路相同 只不过 dfs 这里返回最大链和
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = -inf
        def dfs(node: TreeNode) -> int:
            if node is None:
                return 0
            l_s = dfs(node.left)
            r_s = dfs(node.right)
            nonlocal ans
            ans = max(ans, l_s + r_s + node.val)
            return max(max(l_s, r_s) + node.val, 0)
        dfs(root)
        return ans








