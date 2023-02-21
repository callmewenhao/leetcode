# -*- coding: utf-8 -*-

"""
@File    : btreeGameWinningMove.py
@Author  : wenhao
@Time    : 2023/2/3 12:46
@LC      : 
"""
from typing import Optional
from Tree import TreeNode


class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        lsz = rsz = 0
        def dfs(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            ls = dfs(node.left)
            rs = dfs(node.right)
            if node.val == x:
                nonlocal lsz, rsz
                lsz, rsz = ls, rs
            return ls + rs + 1
        dfs(root)
        return max(lsz, rsz, n - 1 - lsz - rsz) * 2 > n










        pass

