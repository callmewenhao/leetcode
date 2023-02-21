# -*- coding: utf-8 -*-

"""
@File    : middleNode.py
@Author  : wenhao
@Time    : 2023/1/31 15:15
@LC      : 876
"""
from typing import Optional
from List import ListNode


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
