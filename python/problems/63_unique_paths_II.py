# https://leetcode.com/problems/unique-paths-ii/
from functools import lru_cache


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        # If the starting cell has an obstacle, then simply return as there would be
        # no paths to the destination.
        if obstacleGrid[0][0] == 1:
            return 0

        # Number of ways of reaching the starting cell = 1.
        obstacleGrid[0][0] = 1

        # Filling the values for the first column
        for i in range(1, m):
            obstacleGrid[i][0] = int(
                obstacleGrid[i][0] == 0 and obstacleGrid[i - 1][0] == 1
            )

        # Filling the values for the first row
        for j in range(1, n):
            obstacleGrid[0][j] = int(
                obstacleGrid[0][j] == 0 and obstacleGrid[0][j - 1] == 1
            )

        # Starting from cell(1,1) fill up the values
        # No. of ways of reaching cell[i][j] = cell[i - 1][j] + cell[i][j - 1]
        # i.e. From above and left.
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    obstacleGrid[i][j] = obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1]
                else:
                    obstacleGrid[i][j] = 0

        # Return value stored in rightmost bottommost cell. That is the destination.
        return obstacleGrid[m - 1][n - 1]


class Solution2:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        if obstacleGrid[m - 1][n - 1] == 1:
            return 0

        @lru_cache
        def dfs(x: int, y: int) -> int:
            if (x, y) == (m - 1, n - 1):
                return 1
            if x >= m or y >= n or obstacleGrid[x][y] == 1:
                return 0
            return dfs(x + 1, y) + dfs(x, y + 1)

        return dfs(0, 0)


if __name__ == '__main__':
    for s in (Solution(), Solution2()):
        assert s.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]) == 2
        assert s.uniquePathsWithObstacles([[0, 1], [0, 0]]) == 1
