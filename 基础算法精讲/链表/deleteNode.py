# -*- coding: utf-8 -*-

"""
@File    : deleteNode.py
@Author  : wenhao
@Time    : 2023/1/31 15:52
@LC      : 273
"""
from typing import Optional
from List import ListNode


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # 偷换概念的做法
        node.val = node.next.val
        node.next = node.next.next
