# -*- coding: utf-8 -*-

"""
@File    : T2.py
@Author  : wenhao
@Time    : 2023/3/5 10:10
@LC      : 
"""
from typing import List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from Tree import TreeNode
from typing import Optional


class Solution:
    # 经典 bfs 双数组
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        ans = []
        l = [root]

        while len(l):
            l_ = []
            s = 0
            for node in l:
                s += node.val
                if node.left:
                    l_.append(node.left)
                if node.right:
                    l_.append(node.right)
            ans.append(s)
            l = l_  # 别忘记这个 😁

        if len(ans) < k:
            return -1

        ans.sort()
        return ans[k - 1]
