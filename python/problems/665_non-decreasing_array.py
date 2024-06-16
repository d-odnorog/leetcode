# https://leetcode.com/problems/non-decreasing-array/


class Solution:
    def checkPossibility(self, nums: list[int]) -> bool:
        is_non_decreasing = False
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                if is_non_decreasing:
                    return False
                is_non_decreasing = True
                if i >= 2 and nums[i - 2] > nums[i]:
                    nums[i] = nums[i - 1]
        return True


if __name__ == '__main__':
    s = Solution()

    assert s.checkPossibility([4, 2, 3])
    assert not s.checkPossibility([4, 2, 1])
