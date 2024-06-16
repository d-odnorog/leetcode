# https://leetcode.com/problems/rotate-array/


class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        nums_copy = nums.copy()
        for i in range(length):
            nums[i] = nums_copy[(i - k) % length]

        # return nums


if __name__ == '__main__':
    s = Solution()

    # assert s.rotate([1, 2, 3, 4, 5, 6, 7], 3) == [5, 6, 7, 1, 2, 3, 4]
    # assert s.rotate([-1, -100, 3, 99], 2) == [3, 99, -1, -100]
    # assert s.rotate([1, 2, 3, 4, 5, 6, 7], 3) == [5, 6, 7, 1, 2, 3, 4]
