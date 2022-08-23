# https://leetcode.com/problems/palindrome-linked-list/
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        s = ''

        while head:
            s += str(head.val)
            head = head.next

        return s == s[::-1]


class Solution2:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        l = []

        while head:
            l.append(head.val)
            head = head.next

        return l == l[::-1]
