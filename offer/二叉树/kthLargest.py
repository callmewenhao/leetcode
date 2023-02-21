# -*- coding: utf-8 -*-

"""
@File    : kthLargest.py
@Author  : wenhao
@Time    : 2023/2/1 12:28
@LC      : 
"""
from Tree import TreeNode


class Solution:
    # 中序遍历二叉搜索树倒序
    def kthLargest(self, root: TreeNode, k: int) -> int:
        self.k = k
        self.ans = -1

        def dfs(root: TreeNode):
            if root is None:
                return
            dfs(root.right)
            if self.k == 0:
                return self.ans
            self.k -= 1
            if self.k == 0:
                self.ans = root.val
            dfs(root.left)

        dfs(root)
        return self.ans

    # 中序遍历二叉搜索树 + list
    def kthLargest(self, root: TreeNode, k: int) -> int:
        buf = []

        def dfs(root: TreeNode):
            if root is None:
                return
            dfs(root.left)
            buf.append(root.val)
            dfs(root.right)

        dfs(root)

        return buf[-k]
