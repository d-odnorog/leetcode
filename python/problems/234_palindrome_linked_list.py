# https://leetcode.com/problems/palindrome-linked-list/


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        s = ''

        while head:
            s += str(head.val)
            head = head.next

        return s == s[::-1]


class Solution2:
    def isPalindrome(self, head: ListNode | None) -> bool:
        lst = []

        while head:
            lst.append(head.val)
            head = head.next

        return lst == lst[::-1]
