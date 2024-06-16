# https://leetcode.com/problems/deepest-leaves-sum/


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deepestLeavesSum(self, root: TreeNode | None) -> int:
        queue = [root]
        while queue:
            last_sum, new_queue = 0, []
            while queue:
                node = queue.pop(0)
                last_sum += node.val
                if any([node.left, node.right]):
                    if node.left:
                        new_queue.append(node.left)
                    if node.right:
                        new_queue.append(node.right)

            queue = new_queue

        return last_sum
