# -*- coding: utf-8 -*-

"""
@File    : findBottomLeftValue.py
@Author  : wenhao
@Time    : 2023/2/3 22:33
@LC      : 513
"""
from typing import List, Optional
from Tree import TreeNode


class Solution:
    # 反向层序遍历：返回最后一个节点的值
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        ans = 0
        q = [root]
        while len(q) != 0:
            nq = []
            for node in q:
                ans = node.val
                if node.right:
                    nq.append(node.right)
                if node.left:
                    nq.append(node.left)
            q = nq
        return ans

    # 正常层序遍历：返回最后一层的第一个节点值
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        ans = 0
        q = [root]
        while len(q) != 0:
            nq = []
            for i, node in enumerate(q):
                if i == 0:
                    ans = node.val
                if node.left:
                    nq.append(node.left)
                if node.right:
                    nq.append(node.right)
            q = nq
        return ans



