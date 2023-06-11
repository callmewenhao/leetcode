# -*- coding: utf-8 -*-

"""
@File    : nextLargerNodes.py
@Author  : wenhao
@Time    : 2023/4/10 9:08
@LC      : 1019
"""
from typing import List, Optional
from List import ListNode
from collections import deque


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        # 反转链表
        cur = head
        pre = None
        while cur:
            t = cur
            cur = cur.next
            t.next = pre
            pre = t

        # 单调栈 找第一个最大值
        st = []
        ans = []
        while pre:
            if not st:
                ans.append(0)
                st.append(pre.val)
            else:
                num = pre.val
                while st and num >= st[-1]:
                    st.pop()
                if not st:
                    ans.append(0)
                else:
                    ans.append(st[-1])
                st.append(num)
            pre = pre.next
        ans.reverse()
        return ans
