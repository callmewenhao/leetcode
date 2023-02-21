# -*- coding: utf-8 -*-

"""
@File    : binaryTreePaths.py
@Author  : wenhao
@Time    : 2023/2/3 16:18
@LC      : 257
"""
from typing import Optional, List
from Tree import TreeNode


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []

        def dfs(node, depth, path):
            if node is None:
                return
            if depth == 0:
                path += str(node.val)
            else:
                path += "->" + str(node.val)
            if node.left is None and node.right is None:
                ans.append(path)
                return

            dfs(node.left, depth + 1, path)
            dfs(node.right, depth + 1, path)
        dfs(root, 0, '')
        return ans

