# -*- coding: utf-8 -*-

"""
@File    : sortedListToBST.py
@Author  : wenhao
@Time    : 2023/2/3 14:43
@LC      : 109
"""
from typing import Optional
from List import ListNode
from Tree import TreeNode


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def dfs(l, r):  # 闭区间
            if l > r:
                return None

            mid = (l + r) // 2
            node = head
            m = mid
            while m:
                m -= 1
                node = node.next

            root = TreeNode(node.val)
            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)

            return root

        # 计算长度
        n = 0
        h = head
        while h:
            n += 1
            h = h.next

        return dfs(0, n - 1)
