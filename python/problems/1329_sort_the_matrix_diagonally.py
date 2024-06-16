# https://leetcode.com/problems/sort-the-matrix-diagonally/
from collections import defaultdict


class Solution:
    def diagonalSort(self, mat: list[list[int]]) -> list[list[int]]:
        m, n = len(mat), len(mat[0])

        d = defaultdict(list)

        for i in range(m):
            for j in range(n):
                d[i - j].append(mat[i][j])

        for k in d:
            d[k].sort(reverse=True)

        for i in range(m):
            for j in range(n):
                mat[i][j] = d[i - j].pop()

        return mat


if __name__ == '__main__':
    s = Solution()

    assert s.diagonalSort([[3, 3, 1, 1], [2, 2, 1, 2], [1, 1, 1, 2]]) == [
        [1, 1, 1, 1],
        [1, 2, 2, 2],
        [1, 2, 3, 3],
    ]
    assert s.diagonalSort(
        [
            [11, 25, 66, 1, 69, 7],
            [23, 55, 17, 45, 15, 52],
            [75, 31, 36, 44, 58, 8],
            [22, 27, 33, 25, 68, 4],
            [84, 28, 14, 11, 5, 50],
        ]
    ) == [
        [5, 17, 4, 1, 52, 7],
        [11, 11, 25, 45, 8, 69],
        [14, 23, 25, 44, 58, 15],
        [22, 27, 31, 36, 50, 66],
        [84, 28, 75, 33, 55, 68],
    ]
