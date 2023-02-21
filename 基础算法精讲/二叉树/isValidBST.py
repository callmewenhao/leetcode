# -*- coding: utf-8 -*-

"""
@File    : isValidBST.py
@Author  : wenhao
@Time    : 2023/2/3 16:29
@LC      : 98
"""
from typing import Optional
from Tree import TreeNode
from math import inf


class Solution:
    # 后序遍历
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def f(node):
            if node is None:
                return inf, -inf
            l_min, l_max = f(node.left)
            r_min, r_max = f(node.right)
            x = node.val
            if x <= l_max or x >= r_min:
                return -inf, inf
            return min(l_min, x), max(r_max, x)
        return f(root)[1] != inf


    # 中序遍历
    pre = -inf
    def isValidBST3(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        if not self.isValidBST(root.left):
            return False
        if root.val <= self.pre:
            return False
        self.pre = root.val
        return self.isValidBST(root.right)



    # dfs 优化
    def isValidBST2(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, l, r):
            if node is None:
                return True
            return l < node.val < r and dfs(node.left, l, node.val) and \
                   dfs(node.right, node.val, r)
        return dfs(root, -inf, inf)


    # dfs
    def isValidBST1(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, l, r):
            if node is None:
                return True
            if not (l < node.val < r):
                return False

            return dfs(node.left, l, node.val) and \
                   dfs(node.right, node.val, r)
        return dfs(root.left, -inf, root.val) and dfs(root.right, root.val, inf)
