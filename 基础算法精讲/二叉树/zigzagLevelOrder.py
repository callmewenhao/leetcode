# -*- coding: utf-8 -*-

"""
@File    : zigzagLevelOrder.py
@Author  : wenhao
@Time    : 2023/2/3 22:20
@LC      : 103
"""
from typing import List, Optional
from Tree import TreeNode


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if root is None:
            return ans
        depth = 0
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
            # if depth % 2:
            #     level.reverse()
            # ans.append(level)
            ans.append(level[::-1] if depth % 2 else level)
            depth += 1
        return ans
