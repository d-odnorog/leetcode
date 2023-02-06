# https://leetcode.com/problems/search-insert-position/
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)

        while start < end:
            pivot = (start + end) // 2
            if nums[pivot] < target:
                start = pivot + 1
            else:
                end = pivot

        return start


if __name__ == '__main__':
    s = Solution()

    assert s.searchInsert([1, 3, 5, 6], 7) == 4
    assert s.searchInsert([1, 3, 5, 6], 5) == 2
    assert s.searchInsert([1, 3, 5, 6], 2) == 1
