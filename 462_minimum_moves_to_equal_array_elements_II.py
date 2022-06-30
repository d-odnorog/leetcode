# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/
from typing import List


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        snums = sorted(nums)

        median = snums[int(len(snums) / 2)]

        min_move_count = 0
        for n in snums:
            min_move_count += abs(n - median)

        return min_move_count


if __name__ == '__main__':
    s = Solution()

    assert s.minMoves2([1, 2, 3]) == 2
    assert s.minMoves2([1, 10, 2, 9]) == 16
