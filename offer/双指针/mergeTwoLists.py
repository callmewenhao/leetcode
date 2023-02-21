# -*- coding: utf-8 -*-

"""
@File    : mergeTwoLists.py
@Author  : wenhao
@Time    : 2023/1/29 19:32
"""
from List import ListNode


class Solution:
    # 修改原来的链表
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur = dum = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next, l1 = l1, l1.next
            else:
                cur.next, l2 = l2, l2.next
            cur = cur.next
        cur.next = l1 if l1 else l2
        return dum.next

    # 构造新节点
    def mergeTwoLists1(self, l1: ListNode, l2: ListNode) -> ListNode:
        h = ListNode(0)
        d = h
        while l1 and l2:
            if l1.val < l2.val:
                d.next = ListNode(l1.val)
                l1 = l1.next
            else:
                d.next = ListNode(l2.val)
                l2 = l2.next
            d = d.next
        if l1:
            d.next = l1
        if l2:
            d.next = l2
        return h.next
