# -*- coding: utf-8 -*-

"""
@File    : maxDepth.py
@Author  : wenhao
@Time    : 2023/2/3 13:44
@LC      : 104
"""
from typing import Optional
from Tree import TreeNode


class Solution:
    # 写法2
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(root: Optional[TreeNode], cnt: int):
            if root is None:
                return
            cnt += 1
            nonlocal ans
            ans = max(ans, cnt)

            dfs(root.left, cnt)
            dfs(root.right, cnt)
        dfs(root, 0)
        return ans

    # 写法1
    def maxDepth1(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
