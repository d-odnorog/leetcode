# https://leetcode.com/problems/running-sum-of-1d-array/


class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        s = 0
        for i, n in enumerate(nums):
            s += n
            nums[i] = s

        return nums


class Solution2:
    def runningSum(self, nums: list[int]) -> list[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums


if __name__ == '__main__':
    for s in (Solution(), Solution2()):
        assert s.runningSum([1, 2, 3, 4]) == [1, 3, 6, 10]
        assert s.runningSum([1, 1, 1, 1, 1]) == [1, 2, 3, 4, 5]
        assert s.runningSum([3, 1, 2, 10, 1]) == [3, 4, 6, 16, 17]
