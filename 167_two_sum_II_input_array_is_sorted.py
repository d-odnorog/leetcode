# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while right > left:
            s = numbers[left] + numbers[right]
            if s == target:
                return [left + 1, right + 1]
            elif s < target:
                left += 1
            else:
                right -= 1


class Solution2:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}  # {value: index}
        for i, n in enumerate(numbers):
            remaining = target - n
            if remaining in seen:
                return [seen[remaining] + 1, i + 1]
            else:
                seen[n] = i


if __name__ == '__main__':
    for s in (Solution(), Solution2()):
        assert s.twoSum([2, 7, 11, 15], 9) == [1, 2]
        assert s.twoSum([2, 3, 4], 6) == [1, 3]
        assert s.twoSum([-1, 0], -1) == [1, 2]
