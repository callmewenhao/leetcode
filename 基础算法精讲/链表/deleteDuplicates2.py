# -*- coding: utf-8 -*-

"""
@File    : deleteDuplicates2.py
@Author  : wenhao
@Time    : 2023/1/31 16:09
@LC      : 82
"""

from typing import Optional
from List import ListNode


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        dummy = ListNode(next=head)
        h = dummy
        while h.next and h.next.next:
            if h.next.val == h.next.next.val:
                val = h.next.val # 记录这个值，把和这个值一样的节点删去
                while h.next and h.next.val == val:
                    h.next = h.next.next
            else:
                h = h.next

        return dummy.next
