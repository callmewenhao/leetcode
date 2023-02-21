# -*- coding: utf-8 -*-

"""
@File    : buildTree.py
@Author  : wenhao
@Time    : 2023/2/7 20:27
@LC      : 
"""
from typing import List
from Tree import TreeNode


class Solution:
    # optimize
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # 不使用 for 循环查找 root 在中序遍历的位置，而是使用 dict 提前保存
        n = len(preorder)
        dic = {}
        for i, num in enumerate(inorder):
            dic[num] = i
        '''
        i: 前序遍历的起点
        l: 中序遍历的起点
        r: 中序遍历的终点
        '''
        def dfs(i, l, r):
            if l > r:
                return None
            val = preorder[i]
            root = TreeNode(val)

            m = dic[val]
            root.left = dfs(i + 1, l, m - 1)
            root.right = dfs(i + (m - l) + 1, m + 1, r)
            return root

        return dfs(0, 0, n - 1)



    def buildTree1(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        n = len(preorder)

        def dfs(pl, pr, il, ir):
            if pl > pr:
                return None
            val = preorder[pl]
            m = 0
            for i in range(il, ir + 1):
                if inorder[i] == val:
                    m = i
                    break
            left_tree_len = m - il
            root = TreeNode(val)
            root.left = dfs(pl + 1, pl + left_tree_len, il, m - 1)
            root.right = dfs(pl + left_tree_len + 1, pr, m + 1, ir)
            return root

        return dfs(0, n - 1, 0, n - 1)
