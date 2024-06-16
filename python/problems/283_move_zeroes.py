# https://leetcode.com/problems/move-zeroes/


class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            if not nums[i]:
                for j in range(i, len(nums)):
                    if nums[j]:
                        nums[i], nums[j] = nums[j], nums[i]
                        break


class Solution2:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ind = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[ind] = nums[i]
                if i > ind:
                    nums[i] = 0
                ind += 1


if __name__ == '__main__':
    for s in (Solution(), Solution2()):
        nums = [0, 1, 0, 3, 12]
        s.moveZeroes(nums)
        assert nums == [1, 3, 12, 0, 0]

        nums = [0]
        s.moveZeroes(nums)
        assert nums == [0]
