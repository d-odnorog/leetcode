# https://leetcode.com/problems/range-sum-query-2d-immutable/
from typing import List


class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.dp = [
            [0] * (len(matrix[0]) + 1)
            for _ in range(len(matrix) + 1)
        ]

        # calculate prefix sum
        for r in range(len(self.dp) - 1):
            for c in range(len(self.dp[0]) - 1):
                self.dp[r + 1][c + 1] = (
                        matrix[r][c]
                        + self.dp[r][c + 1]
                        + self.dp[r + 1][c]
                        - self.dp[r][c]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
                self.dp[row2 + 1][col2 + 1]
                - self.dp[row1][col2 + 1]
                - self.dp[row2 + 1][col1]
                + self.dp[row1][col1]
        )


if __name__ == '__main__':
    obj = NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
    assert obj.sumRegion(2, 1, 4, 3) == 8
    assert obj.sumRegion(1, 1, 2, 2) == 11
    assert obj.sumRegion(1, 2, 2, 4) == 12
