# -*- coding: utf-8 -*-

"""
@File    : reorderList.py
@Author  : wenhao
@Time    : 2023/1/31 15:29
@LC      : 143
"""
from typing import Optional
from List import ListNode


class Solution:
    # 反转链表
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre, cur = None, head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre

    # 求中间节点
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        m = self.middleNode(head)
        h2 = self.reverseList(m)

        while h2.next:
            n1 = head.next
            n2 = h2.next

            head.next = h2
            h2.next = n1
            head = n1
            h2 = n2

