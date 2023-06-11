# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional, Tuple
from List import ListNode
from collections import defaultdict


class Solution:

    # 前缀和 + hash优化
    # 第一次遍历确定 last 位置
    # 第二次遍历确定 节点指向
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        dict = defaultdict(ListNode)

        s = 0
        cur = dummy
        while cur:
            s += cur.val
            dict[s] = cur
            cur = cur.next

        s = 0
        cur = dummy
        while cur:
            s += cur.val
            if s in dict:
                cur.next = dict[s].next
            cur = cur.next

        return dummy.next

    # 朴素做法 On^2

    def removeZeroSumSublists1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        sum = 0
        cur = dummy
        st = []

        def find(s: int) -> Tuple[int, ListNode]:
            for i, (val, node) in enumerate(st):
                if val == s:
                    return i, node
            return -1, None

        while cur:
            sum += cur.val

            idx, node = find(sum)
            if idx != -1:
                node.next = cur.next
                st = st[:idx+1]
            else:
                st.append((sum, cur))

            cur = cur.next
        return dummy.next
