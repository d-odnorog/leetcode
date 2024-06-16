# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode | None) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def rightmost(root):
            if root.right:
                return rightmost(root.right)
            return root

        while root:
            if root.left:
                rightMOST = rightmost(root.left)
                nextright = root.right
                root.right = root.left
                root.left = None
                rightMOST.right = nextright

            root = root.right
