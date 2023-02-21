# -*- coding: utf-8 -*-

"""
@File    : mergeInBetween.py
@Author  : wenhao
@Time    : 2023/1/30 10:10
"""
from List import ListNode


class Solution:
    def mergeInBetween(self, l1: ListNode, a: int, b: int, l2: ListNode) -> ListNode:
        h1, h2 = l1, l2
        while a > 1:
            h1 = h1.next
            a -= 1
            b -= 1
        t = h1.next
        h1.next = h2
        while b > 1:
            t = t.next
            b -= 1
        while h2.next:
            h2 = h2.next
        h2.next = t.next
        return l1

