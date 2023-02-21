# -*- coding: utf-8 -*-

"""
@File    : getIntersectionNode.py
@Author  : wenhao
@Time    : 2023/1/29 19:58
"""
from List import ListNode


class Solution:
    # 遍历两边链表
    def getIntersectionNode(self, ha: ListNode, hb: ListNode) -> ListNode:
        n1, n2 = ha, hb
        while n1 != n2:
            n1 = n1.next if n1 else hb
            n2 = n2.next if n2 else ha

        return n1

    # 使用集合的写法
    def getIntersectionNode1(self, ha: ListNode, hb: ListNode) -> ListNode:
        s = set()
        while ha:
            s.add(ha)
            ha = ha.next
        ans = None
        while hb:
            if hb in s:
                ans = hb
                break
            hb = hb.next
        return ans
