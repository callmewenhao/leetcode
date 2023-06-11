# -*- coding: utf-8 -*-

"""
@File    : maxAncestorDiff.py
@Author  : wenhao
@Time    : 2023/4/18 8:44
@LC      : 1026
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
from Tree import TreeNode
from math import inf


class Solution:
    # 优化
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ans = 0  # ans 最小也就是 0

        def dfs(node: TreeNode) -> (int, int):
            if node is None:
                return inf, -inf
            # 处理答案
            nonlocal ans
            l_mn, l_mx = dfs(node.left)
            r_mn, r_mx = dfs(node.right)
            x1, y1 = abs(node.val - l_mn), abs(node.val - l_mx)
            x2, y2 = abs(node.val - r_mn), abs(node.val - r_mx)
            arr = [x1, x2, y1, y2]
            for x in arr:
                if x != inf:
                    ans = max(ans, x)
            return min(l_mn, r_mn, node.val), max(l_mx, r_mx, node.val)

        dfs(root)
        return ans

    # 有些树形 DP 味道
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(node: TreeNode) -> (int, int):  # 返回 mn, mx
            if node.left is None and node.right is None:
                return node.val, node.val

            nonlocal ans
            mn, mx = inf, -inf
            if node.left:
                res1 = dfs(node.left)
                mn = min(mn, res1[0])
                mx = max(mx, res1[1])
            if node.right:
                res2 = dfs(node.right)
                mn = min(mn, res2[0])
                mx = max(mx, res2[1])
            ans = max(ans, abs(node.val - mn), abs(node.val - mx))

            return min(mn, node.val), max(mx, node.val)

        dfs(root)
        return ans
