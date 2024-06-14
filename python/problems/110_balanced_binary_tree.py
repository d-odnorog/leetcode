# https://leetcode.com/problems/balanced-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isBalanced(self, root):
        if root is None:
            return True

        left = self.depth(root.left)
        right = self.depth(root.right)
        return (
            abs(left - right) < 2
            and self.isBalanced(root.left)
            and self.isBalanced(root.right)
        )

    def depth(self, node):
        if node is None:
            return 0

        return max(self.depth(node.left), self.depth(node.right)) + 1
