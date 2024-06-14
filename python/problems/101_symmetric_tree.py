# https://leetcode.com/problems/symmetric-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSymmetric(self, root):
        if not root:
            return True

        return self.isSame(root.left, root.right)

    def isSame(self, left_root, right_root):
        if left_root is None and right_root is None:
            return True
        elif left_root is None or right_root is None:
            return False
        elif left_root.val != right_root.val:
            return False

        return self.isSame(left_root.left, right_root.right) and self.isSame(left_root.right, right_root.left)
