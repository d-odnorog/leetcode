# https://leetcode.com/problems/intersection-of-two-linked-lists/
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        first_set = set()

        current_node = headA
        while current_node:
            first_set.add(current_node)
            current_node = current_node.next

        current_node = headB
        while current_node:
            if current_node in first_set:
                return current_node
            current_node = current_node.next

        return None


class Solution2:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        one = headA
        two = headB

        while one != two:
            one = headB if one is None else one.next
            two = headA if two is None else two.next
        return one
