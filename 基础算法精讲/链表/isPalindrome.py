# -*- coding: utf-8 -*-

"""
@File    : isPalindrome.py
@Author  : wenhao
@Time    : 2023/1/31 16:33
@LC      : 234
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
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        mid =self.middleNode(head)
        h = self.reverseList(mid)
        while h:
            if h.val != head.val:
                return False
            h = h.next
            head = head.next
        return True





