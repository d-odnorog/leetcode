# https://leetcode.com/problems/pacific-atlantic-water-flow/
from typing import List, Set, Tuple


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def pac(i, j):
            if rp[i][j]:
                return True
            k = False
            h = heights[i][j]
            heights[i][j] = 100001
            if heights[i - 1][j] <= h:
                k = k or pac(i - 1, j)

            if heights[i][j - 1] <= h:
                k = k or pac(i, j - 1)

            if i < m - 1 and heights[i + 1][j] <= h:
                k = k or pac(i + 1, j)

            if j < n - 1 and heights[i][j + 1] <= h:
                k = k or pac(i, j + 1)

            heights[i][j] = h
            rp[i][j] = k
            return k

        def atl(i, j):
            if ra[i][j]:
                return True
            k = False
            h = heights[i][j]
            heights[i][j] = 100001
            if i > 0 and heights[i - 1][j] <= h:
                k = k or atl(i - 1, j)

            if j > 0 and heights[i][j - 1] <= h:
                k = k or atl(i, j - 1)

            if heights[i + 1][j] <= h:
                k = k or atl(i + 1, j)

            if heights[i][j + 1] <= h:
                k = k or atl(i, j + 1)

            heights[i][j] = h
            ra[i][j] = k
            return k

        m = len(heights)
        n = len(heights[0])
        rp = [[False for i in range(n)] for j in range(m)]
        ra = [[False for i in range(n)] for j in range(m)]

        for i in range(m):
            rp[i][0] = True
            ra[i][-1] = True
        for i in range(n):
            rp[0][i] = True
            ra[-1][i] = True

        for i in range(m):
            for j in range(n):
                pac(i, j)
                atl(i, j)
        res = []
        for i in range(m):
            for j in range(n):
                if rp[i][j] and ra[i][j]:
                    res.append([i, j])
        return res


class Solution2:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])

        def dfs(i: int, j: int, prev_height: int, coords: Set[Tuple[int]]) -> None:
            if i < 0 or i == m or j < 0 or j == n:
                # out of bounds
                return

            if (i, j) in coords:
                # already visited
                return

            height = heights[i][j]

            if height < prev_height:
                # water can't flow to a higher height
                return

            # ocean is reachable from current coordinate
            coords.add((i, j))

            # all four directions
            dfs(i + 1, j, height, coords)
            dfs(i - 1, j, height, coords)
            dfs(i, j + 1, height, coords)
            dfs(i, j - 1, height, coords)

        pacific_coords = set()

        # top row
        for j in range(n):
            dfs(0, j, 0, pacific_coords)

        # left col
        for i in range(m):
            dfs(i, 0, 0, pacific_coords)

        atlantic_coords = set()

        # right col
        for i in range(m):
            dfs(i, n - 1, 0, atlantic_coords)

        # bottom row
        for j in range(n):
            dfs(m - 1, j, 0, atlantic_coords)

        # intersection of coords reachable from both Pacific and Atlantic
        return list(pacific_coords & atlantic_coords)


if __name__ == '__main__':
    s = Solution()
    assert s.pacificAtlantic(
        [
            [1, 2, 2, 3, 5],
            [3, 2, 3, 4, 4],
            [2, 4, 5, 3, 1],
            [6, 7, 1, 4, 5],
            [5, 1, 1, 2, 4],
        ]
    ) == sorted([[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]])
    assert s.pacificAtlantic([[1]]) == [[0, 0]]

    s2 = Solution2()
    assert sorted(
        s2.pacificAtlantic(
            [
                [1, 2, 2, 3, 5],
                [3, 2, 3, 4, 4],
                [2, 4, 5, 3, 1],
                [6, 7, 1, 4, 5],
                [5, 1, 1, 2, 4],
            ]
        )
    ) == sorted([(0, 4), (1, 3), (1, 4), (2, 2), (3, 0), (3, 1), (4, 0)])
    assert s2.pacificAtlantic([[1]]) == [(0, 0)]
