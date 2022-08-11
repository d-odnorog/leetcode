# https://leetcode.com/problems/validate-binary-search-tree/
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid_bst(root, min_val, max_val):
            if root is None:
                return True
            if root.val <= min_val or root.val >= max_val:
                return False

            return valid_bst(root.left, min_val, root.val) and valid_bst(
                root.right, root.val, max_val
            )

        return valid_bst(root, -(2**31) - 1, 2**31)
