# -*- coding: utf-8 -*-

"""
@File    : detectCycle.py
@Author  : wenhao
@Time    : 2023/1/31 15:27
@LC      : 142
"""
from typing import Optional
from List import ListNode


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                while head is not slow:
                    slow = slow.next
                    head = head.next
                return slow

        return None
