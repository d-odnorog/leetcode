# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
from bisect import bisect
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        low = matrix[0][0]
        high = matrix[-1][-1]

        while low < high:
            mid = low + (high - low) // 2
            if (
                sum(bisect(row, mid) for row in matrix) < k
            ):  # how many numbers are on the left of middle number
                low = mid + 1
            else:
                high = mid

        return low


if __name__ == '__main__':
    s = Solution()

    assert s.kthSmallest([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8) == 13
    assert s.kthSmallest([[-5]], 1) == -5
