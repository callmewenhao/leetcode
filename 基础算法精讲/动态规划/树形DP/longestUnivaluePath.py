# -*- coding: utf-8 -*-

"""
@File    : longestUnivaluePath.py
@Author  : wenhao
@Time    : 2023/4/18 9:26
@LC      : 687
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
    # 优化 灵神 NB🙂
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        ans = 0

        # 以 node 为跟的最长链
        def dfs(node: TreeNode) -> int:
            if node is None:
                return -1
            l_len = dfs(node.left) + 1  # 左边最大链长 + 1
            r_len = dfs(node.right) + 1  # 右边最大链长 + 1

            if node.left and node.left.val != node.val:  # 改成 0
                l_len = 0
            if node.right and node.right.val != node.val:
                r_len = 0
            # 更新答案
            nonlocal ans
            ans = max(ans, l_len + r_len)  # 拼成一条路径 更新答案

            return max(l_len, r_len)  # 返回最大链长

        dfs(root)
        return ans

    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        ans = 0

        # 以 node 为跟的最长链
        def dfs(node: TreeNode) -> int:
            l_len = r_len = 0
            if node is None:
                return 0
            if node.left:
                l_len = dfs(node.left)
            if node.right:
                r_len = dfs(node.right)

            # 更新答案
            res1 = res2 = 0
            if node.left and node.val == node.left.val:
                res1 += l_len + 1
            if node.right and node.val == node.right.val:
                res2 += r_len + 1
            nonlocal ans
            ans = max(ans, res1 + res2)

            # 返回值
            return max(res1, res2)

        dfs(root)
        return ans
