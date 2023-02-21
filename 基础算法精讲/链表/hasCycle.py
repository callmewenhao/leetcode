# -*- coding: utf-8 -*-

"""
@File    : hasCycle.py
@Author  : wenhao
@Time    : 2023/1/31 15:20
@LC      : 141
"""
from typing import Optional
from List import ListNode



class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True

        return False

