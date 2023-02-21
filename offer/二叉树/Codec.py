# -*- coding: utf-8 -*-

"""
@File    : Codec.py
@Author  : wenhao
@Time    : 2023/2/16 20:04
@LC      : 297
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from Tree import TreeNode


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""

        ans = ""
        q = [root]

        while len(q):
            n_q = []
            for node in q:
                if not node:
                    ans += "null"
                else:
                    ans += str(node.val)
                    n_q.append(node.left)
                    n_q.append(node.right)
                ans += ' '
            q = n_q
        return ans

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        nodes = data.split(" ")
        root = TreeNode(int(nodes[0]))
        i, q = 1, [root]

        while len(q):
            n_q = []
            for node in q:
                if nodes[i] == "null":
                    node.left = None
                else:
                    node.left = TreeNode(int(nodes[i]))
                    n_q.append(node.left)
                i += 1

                if nodes[i] == "null":
                    node.right = None
                else:
                    node.right = TreeNode(int(nodes[i]))
                    n_q.append(node.right)
                i += 1
            q = n_q
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
