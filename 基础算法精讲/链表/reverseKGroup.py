# -*- coding: utf-8 -*-

"""
@File    : reverseKGroup.py
@Author  : wenhao
@Time    : 2023/1/31 14:36
@LC      : 25
"""
from typing import Optional
from List import ListNode


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        # 计算长度
        n = 0
        h = head
        while h:
            n += 1
            h = h.next

        # 准备哨兵节点
        dummy = ListNode(next=head)

        h0 = dummy
        pre = None
        cur = h0.next

        # 开始反转
        while n >= k:
            n -= k
            for _ in range(k):  # 反转 k 次
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt
            # 为下次反转做准备
            new_h0 = h0.next
            h0.next.next = cur
            h0.next = pre
            h0 = new_h0

        return dummy.next
