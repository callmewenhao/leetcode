# -*- coding: utf-8 -*-

"""
@File    : treeToDoublyList.py
@Author  : wenhao
@Time    : 2023/2/1 12:16
@LC      : 
"""


# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        buf = []

        def dfs(node: 'Node'):
            if node is Node:
                return

            if node.left:
                dfs(node.left)
            buf.append(node)
            if node.right:
                dfs(node.right)

        dfs(root)
        if len(buf) == 1:
            return root
        for i in range(len(buf)):
            if i == 0:
                buf[i].left = buf[-1]
                buf[i].right = buf[1]
            elif i == len(buf) - 1:
                buf[i].left = buf[i - 1]
                buf[i].right = buf[0]
            else:
                buf[i].left = buf[i - 1]
                buf[i].right = buf[i + 1]
        return root
