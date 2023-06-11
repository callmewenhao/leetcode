# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional
from List import ListNode
from collections import defaultdict


class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        dict = defaultdict(int)

        sum = 0
        cur = dummy
        st = []
        while cur:
            sum += cur.val
            
            if sum in dict:
                st[dict[sum]].next = cur.next
                st = st[:dict[sum]+1]
                dict.pop(sum)
            else:
                dict[sum] = len(st)
                st.append(cur)
            
            cur = cur.next
        return dummy.next
