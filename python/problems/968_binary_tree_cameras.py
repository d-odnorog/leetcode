# https://leetcode.com/problems/binary-tree-cameras/


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minCameraCover(self, root: TreeNode | None) -> int:
        def solve(node):
            # 0: Strict ST; All nodes below this are covered, but not this one
            # 1: Normal ST; All nodes below and incl this are covered - no camera
            # 2: Placed camera; All nodes below this are covered, plus camera here

            if not node:
                return 0, 0, float('inf')

            L = solve(node.left)
            R = solve(node.right)

            dp0 = L[1] + R[1]
            dp1 = min(L[2] + min(R[1:]), R[2] + min(L[1:]))
            dp2 = 1 + min(L) + min(R)

            return dp0, dp1, dp2

        return min(solve(root)[1:])


class Solution2:
    def minCameraCover(self, root):
        self.ans = 0
        covered = {None}

        def dfs(node, par=None):
            if node:
                dfs(node.left, node)
                dfs(node.right, node)

                if (
                    par is None
                    and node not in covered
                    or node.left not in covered
                    or node.right not in covered
                ):
                    self.ans += 1
                    covered.update({node, par, node.left, node.right})

        dfs(root)
        return self.ans
