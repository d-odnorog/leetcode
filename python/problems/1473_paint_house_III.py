# https://leetcode.com/problems/paint-house-iii/
from functools import lru_cache


class Solution:
    def minCost(
        self, houses: list[int], cost: list[list[int]], m: int, n: int, target: int
    ) -> int:
        @lru_cache
        def dp(i, p, h):
            if (h > target) or (i == m and h != target):
                return float('inf')
            if i == m:
                return 0
            if houses[i] != 0:
                return dp(i + 1, houses[i], h + int(p != houses[i]))

            best = float('inf')
            for j, c in enumerate(cost[i], 1):
                best = min(best, dp(i + 1, j, h + int(p != j)) + c)
            return best

        res = dp(0, 0, 0)
        return res if res != float('inf') else -1


if __name__ == '__main__':
    s = Solution()

    assert (
        s.minCost(
            [0, 0, 0, 0, 0], [[1, 10], [10, 1], [10, 1], [1, 10], [5, 1]], 5, 2, 3
        )
        == 9
    )
    assert (
        s.minCost(
            [0, 2, 1, 2, 0], [[1, 10], [10, 1], [10, 1], [1, 10], [5, 1]], 5, 2, 3
        )
        == 11
    )
    assert (
        s.minCost([3, 1, 2, 3], [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]], 4, 3, 3)
        == -1
    )
