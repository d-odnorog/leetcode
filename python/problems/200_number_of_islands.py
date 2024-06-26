# https://leetcode.com/problems/number-of-islands/


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        def dfs(grid, i, j):
            if (
                i < 0
                or j < 0
                or i >= len(grid)
                or j >= len(grid[0])
                or grid[i][j] != '1'
            ):
                return

            grid[i][j] = '#'

            dfs(grid, i + 1, j)
            dfs(grid, i - 1, j)
            dfs(grid, i, j + 1)
            dfs(grid, i, j - 1)

        count = 0

        if not grid:
            return 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(grid, i, j)
                    count += 1

        return count


if __name__ == '__main__':
    s = Solution()

    assert (
        s.numIslands(
            [
                ['1', '1', '1', '1', '0'],
                ['1', '1', '0', '1', '0'],
                ['1', '1', '0', '0', '0'],
                ['0', '0', '0', '0', '0'],
            ]
        )
        == 1
    )
    assert (
        s.numIslands(
            [
                ['1', '1', '0', '0', '0'],
                ['1', '1', '0', '0', '0'],
                ['0', '0', '1', '0', '0'],
                ['0', '0', '0', '1', '1'],
            ]
        )
        == 3
    )
