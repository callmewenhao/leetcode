# -*- coding: utf-8 -*-

"""
@File    : reverseList.py
@Author  : wenhao
@Time    : 2023/1/31 14:12
@LC      : 206
"""
from typing import Optional
from List import ListNode


class Solution:

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        使用三个指针 pre cur nxt
        pre 指向反转好的链表
        cur 指待反转的节点
        nxt 指待反转的节点的下一个节点
        :param head:
        :return:
        """
        pre = None
        cur = head

        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt

        return pre
