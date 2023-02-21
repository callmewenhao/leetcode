# -*- coding: utf-8 -*-

"""
@File    : deleteDuplicates.py
@Author  : wenhao
@Time    : 2023/1/31 16:03
@LC      : 83
"""
from typing import Optional
from List import ListNode


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        h = head
        while h.next:
            if h.next.val == h.val:
                h.next = h.next.next
            else:
                h = h.next
        return head
