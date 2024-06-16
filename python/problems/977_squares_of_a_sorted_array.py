# https://leetcode.com/problems/squares-of-a-sorted-array/


class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        nums = map(lambda x: x**2, nums)
        return sorted(nums)


class Solution2:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        pointer_1 = 0
        pointer_2 = len(nums) - 1
        results = []

        while pointer_1 <= pointer_2:
            if abs(nums[pointer_1]) < abs(nums[pointer_2]):
                results.append(nums[pointer_2] ** 2)
                pointer_2 -= 1
            else:
                results.append(nums[pointer_1] ** 2)
                pointer_1 += 1

        return results[::-1]


if __name__ == '__main__':
    for s in (Solution(), Solution2()):
        assert s.sortedSquares([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100]
        assert s.sortedSquares([-7, -3, 2, 3, 11]) == [4, 9, 9, 49, 121]
