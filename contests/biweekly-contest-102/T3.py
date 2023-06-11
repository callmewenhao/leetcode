# -*- coding: utf-8 -*-

"""
@File    : T3.py
@Author  : wenhao
@Time    : 2023/4/15 22:24
@LC      : 
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
    # 优化 站在父节点的角度处理子节点的值 👍
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        root.val = 0
        q = [root]
        while q:
            temp = q
            q = []
            next_level_sum = 0
            for node in temp:
                if node.left:
                    q.append(node.left)
                    next_level_sum += node.left.val
                if node.right:
                    q.append(node.right)
                    next_level_sum += node.right.val
            for node in temp:
                children_sum = (node.left.val if node.left else 0) \
                               + (node.right.val if node.right else 0)
                if node.left: node.left.val = next_level_sum - children_sum
                if node.right: node.right.val = next_level_sum - children_sum

        return root

    def replaceValueInTree1(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = [(root, None)]

        while len(q):
            new_q = []
            old_val = [node.val for node, _ in q]
            n = len(old_val)
            s = sum(old_val)
            for i, (node, fa) in enumerate(q):
                bro_val = 0
                for j in range(i - 1, i + 2):
                    if 0 <= j < n and q[j][1] == fa:
                        bro_val += old_val[j]
                node.val = s - bro_val
                if node.left:
                    new_q.append((node.left, node))
                if node.right:
                    new_q.append((node.right, node))
            q = new_q

        return root
