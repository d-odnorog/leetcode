# https://leetcode.com/problems/construct-string-from-binary-tree/description/
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ''

        if root.left or root.right:
            left = f'({self.tree2str(root.left)})'
        else:
            left = ''

        if root.right:
            right = f'({self.tree2str(root.right)})'
        else:
            right = ''

        return f'{root.val}{left}{right}'
