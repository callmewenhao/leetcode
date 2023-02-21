# -*- coding: utf-8 -*-

"""
@File    : isSameTree.py
@Author  : wenhao
@Time    : 2023/2/3 13:51
@LC      : 100
"""
from typing import Optional
from Tree import TreeNode


class Solution:
    # 另一种写法
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None or q is None:
            return p == q
        return p.val == q.val and \
               self.isSameTree(p.left, q.left) and \
               self.isSameTree(p.right, q.right)

    def isSameTree1(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        elif p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False
