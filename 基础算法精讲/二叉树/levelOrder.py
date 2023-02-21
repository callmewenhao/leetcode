# -*- coding: utf-8 -*-

"""
@File    : levelOrder.py
@Author  : wenhao
@Time    : 2023/2/3 22:15
@LC      : 102
"""
from typing import List, Optional
from Tree import TreeNode


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if root is None:
            return ans
        q = [root]
        while len(q) != 0:
            nq = []
            level = []
            for node in q:
                level.append(node.val)
                if node.left:
                    nq.append(node.left)
                if node.right:
                    nq.append(node.right)
            q = nq
            ans.append(level)
        return ans






