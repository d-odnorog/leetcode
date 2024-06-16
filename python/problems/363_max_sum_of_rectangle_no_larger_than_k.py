# https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/
from bisect import bisect_left, insort


class Solution:
    def maxSumSubmatrix(self, matrix: list[list[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        res = -float('inf')

        for l in range(n):
            rowSums = [0] * m
            for r in range(l, n):
                colSums = [0]
                colSum = 0
                for i in range(m):
                    rowSums[i] += matrix[i][r]
                    colSum += rowSums[i]
                    diff = colSum - k
                    idx = bisect_left(colSums, diff)
                    if idx < len(colSums):
                        if colSums[idx] == diff:
                            return k
                        else:
                            res = max(res, colSum - colSums[idx])
                    insort(colSums, colSum)

        return res


if __name__ == '__main__':
    s = Solution()

    assert s.maxSumSubmatrix([[1, 0, 1], [0, -2, 3]], 2) == 2
    assert s.maxSumSubmatrix([[2, 2, -1]], 3) == 3
