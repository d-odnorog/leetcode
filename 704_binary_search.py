# https://leetcode.com/problems/binary-search/
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length = len(nums)
        if length == 1:
            return -1 if nums[0] != target else 0
        elif length == 2:
            if nums[0] == target:
                return 0
            elif nums[1] == target:
                return 1
            else:
                return -1

        middle_position = int(len(nums) / 2)
        middle_element = nums[middle_position]
        if middle_element == target:
            return middle_position
        elif middle_element < target:
            result = self.search(nums[middle_position:], target)
            return result + middle_position if result != -1 else result
        else:
            return self.search(nums[:middle_position], target)


class Solution2:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            pivot = left + (right - left) // 2
            if nums[pivot] == target:
                return pivot
            if target < nums[pivot]:
                right = pivot - 1
            else:
                left = pivot + 1
        return -1


if __name__ == '__main__':
    s = Solution()

    for s in (Solution(), Solution2()):
        assert s.search([-1, 0, 3, 5, 9, 12], 9) == 4
        assert s.search([-1, 0, 3, 5, 9, 12], 2) == -1
        assert s.search([5], 5) == 0
        assert s.search([2, 5], 2) == 0
        assert s.search([2, 5], 4) == -1
        assert s.search([-1, 0, 5], -1) == 0
