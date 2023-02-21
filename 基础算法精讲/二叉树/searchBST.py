# -*- coding: utf-8 -*-

"""
@File    : searchBST.py
@Author  : wenhao
@Time    : 2023/2/3 21:39
@LC      : 700
"""
from typing import List, Optional
from Tree import TreeNode


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return None

        if root.val == val:
            return root

        return self.searchBST(root.right, val) if val > root.val else self.searchBST(root.left, val)





