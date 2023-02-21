# -*- coding: utf-8 -*-

"""
@File    : swapPairs.py
@Author  : wenhao
@Time    : 2023/1/31 16:39
@LC      : 24
"""
from typing import Optional
from List import ListNode


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        h = dummy

        while h.next and h.next.next:
            n1 = h.next
            n2 = h.next.next.next

            h.next = h.next.next
            h.next.next = n1
            h.next.next.next = n2

            h = h.next.next

        return dummy.next

