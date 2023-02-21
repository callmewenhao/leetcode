# -*- coding: utf-8 -*-

"""
@File    : reverseBetween.py
@Author  : wenhao
@Time    : 2023/1/31 14:20
@LC      : 92
"""
from typing import Optional
from List import ListNode


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        """
        使用和反转链表一样的思路
        找到待反转的第一个节点的上一个节点， 反转 right - left + 1 次
        注意：由于可能要反转头节点，此时需要使用一个哨兵节点
        """
        dummy = ListNode(next=head)

        h0 = dummy
        for _ in range(left - 1):
            h0 = h0.next
        pre = None
        cur = h0.next

        for _ in range(right - left + 1):
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt

        h0.next.next = cur
        h0.next = pre
        return dummy.next
