# -*- coding: utf-8 -*-

"""
@File    : kthSmallest.py
@Author  : wenhao
@Time    : 2023/2/3 17:10
@LC      : 230
"""
from typing import Optional
from Tree import TreeNode


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt = k
        ans = 0

        def dfs(node):
            if node is None:
                return
            nonlocal cnt, ans
            dfs(node.left)
            # if cnt == 0:
            #     return
            cnt -= 1
            if cnt == 0:
                ans = node.val
                return
            dfs(node.right)

        dfs(root)
        return ans
