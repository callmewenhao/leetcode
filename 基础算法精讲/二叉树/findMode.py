# -*- coding: utf-8 -*-

"""
@File    : findMode.py
@Author  : wenhao
@Time    : 2023/2/3 17:22
@LC      : 501
"""
from typing import Optional, List
from Tree import TreeNode
from collections import Counter

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        base = 0
        cnt = 0
        ans = []
        maxCnt = -1

        def dfs(node):
            nonlocal cnt, ans, maxCnt, base
            if node is None:
                return
            dfs(node.left)

            if cnt == 0 or base != node.val:
                cnt = 1
                base = node.val
            else:
                cnt += 1

            if cnt == maxCnt:
                ans.append(node.val)
            if cnt > maxCnt:
                ans = [node.val]
                maxCnt = cnt

            dfs(node.right)

        dfs(root)
        return ans

