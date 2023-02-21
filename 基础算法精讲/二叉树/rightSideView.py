# -*- coding: utf-8 -*-

"""
@File    : rightSideView.py
@Author  : wenhao
@Time    : 2023/2/3 15:00
@LC      : 199
"""
from typing import List, Optional
from Tree import TreeNode


class Solution:
    # bfs
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        ans = []
        q = [root]
        while len(q):
            ans.append(q[-1].val)
            nq = []
            for node in q:
                if node.left:
                    nq.append(node.left)
                if node.right:
                    nq.append(node.right)
            q = nq
        return ans



    # dfs
    def rightSideView1(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def dfs(node, depth):
            if node is None:
                return
            if depth == len(ans):
                ans.append(node.val)
            dfs(node.right, depth+1)
            dfs(node.left, depth+1)
        dfs(root, 0)
        return ans
