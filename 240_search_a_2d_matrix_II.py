# https://leetcode.com/problems/search-a-2d-matrix-ii/
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix) - 1, 0  # <-- start at corner

        while row >= 0 and col <= len(matrix[0]) - 1:
            cell = matrix[row][col]

            if cell > target:  # <-- go up
                row -= 1
            elif cell < target:  # <-- go right
                col += 1
            else:
                return True  # <-- target found

        return False


if __name__ == '__main__':
    s = Solution()

    assert s.searchMatrix(
        [
            [1, 4, 7, 11, 15],
            [2, 5, 8, 12, 19],
            [3, 6, 9, 16, 22],
            [10, 13, 14, 17, 24],
            [18, 21, 23, 26, 30],
        ],
        5,
    )
    assert not s.searchMatrix(
        [
            [1, 4, 7, 11, 15],
            [2, 5, 8, 12, 19],
            [3, 6, 9, 16, 22],
            [10, 13, 14, 17, 24],
            [18, 21, 23, 26, 30],
        ],
        20,
    )
