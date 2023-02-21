# -*- coding: utf-8 -*-

"""
@File    : pathSum.py
@Author  : wenhao
@Time    : 2023/2/1 11:58
@LC      :
"""
from Tree import TreeNode
from typing import List


class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        ans = []
        if root is None:
            return ans
        path = []

        def dfs(node: TreeNode, s: int):
            if node is None:
                return

            s += node.val
            path.append(node.val)

            if s == target and node.left is None and node.right is None:
                ans.append(path.copy())
                path.pop()
                return

            if node.left:
                dfs(node.left, s)
            if node.right:
                dfs(node.right, s)

            path.pop()

        dfs(root, 0)
        return ans

