# -*- coding: utf-8 -*-

"""
@File    : removeElements.py
@Author  : wenhao
@Time    : 2023/1/31 16:29
@LC      : 203
"""
from typing import Optional
from List import ListNode


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        h = dummy
        while h.next:
            if val == h.next.val:
                h.next = h.next.next
            else:
                h = h.next
        return dummy.next
