# https://leetcode.com/problems/shuffle-the-array/
from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        for i in range(n):
            result.append(nums[i])
            result.append(nums[n + i])

        return result


class Solution2:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        for i, j in zip(nums[:n], nums[n:]):
            res += [i, j]
        return res


if __name__ == '__main__':
    for s in (Solution(), Solution2()):
        assert s.shuffle([2, 5, 1, 3, 4, 7], 3) == [2, 3, 5, 4, 1, 7]
        assert s.shuffle([1, 2, 3, 4, 4, 3, 2, 1], 4) == [1, 4, 2, 3, 3, 2, 4, 1]
        assert s.shuffle([1, 1, 2, 2], 2) == [1, 2, 1, 2]
