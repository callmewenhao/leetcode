# -*- coding: utf-8 -*-

"""
@File    : removeNthFromEnd.py
@Author  : wenhao
@Time    : 2023/1/31 15:57
@LC      : 19
"""
from typing import Optional
from List import ListNode


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        slow = fast = dummy
        for _ in range(n):
            fast = fast.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next
