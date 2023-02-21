# -*- coding: utf-8 -*-

"""
@File    : lowestCommonAncestor.py
@Author  : wenhao
@Time    : 2023/2/3 21:54
@LC      : 236
"""
from typing import List, Optional
from Tree import TreeNode


class Solution:
    '''
    这个题注意分类讨论
    并且：指针空代表没找到、指针不空代表找到了 p or q，所以要分类讨论
    '''
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None or root is p or root is q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        if left:
            return left
        return right





