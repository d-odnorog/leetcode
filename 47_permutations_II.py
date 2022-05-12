# https://leetcode.com/problems/permutations-ii/
from itertools import permutations
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        perm = permutations(nums)
        result = []
        for p in perm:
            if list(p) not in result:
                result.append(list(p))
        return result


class Solution2:
    def permutation(self, nums):
        if len(nums) == 1:
            return [nums]
        result = []
        for i in range(len(nums)):
            element = nums[i]
            remaining_list = nums[:i] + nums[i + 1:]
            for p in self.permutation(remaining_list):
                if [element] + p not in result:
                    result.append([element] + p)
        return result

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = self.permutation(nums)
        return result


if __name__ == '__main__':
    for s in (Solution(), Solution2()):
        assert s.permuteUnique([1, 1, 2]) == [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
        assert s.permuteUnique([1, 2, 3]) == [
            [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]
        ]
