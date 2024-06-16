# https://leetcode.com/problems/longest-consecutive-sequence/


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0

        nums.sort()

        longest_consecutive = current_consecutive = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                if nums[i] == nums[i - 1] + 1:
                    current_consecutive += 1
                else:
                    longest_consecutive = max(longest_consecutive, current_consecutive)
                    current_consecutive = 1

        return max(longest_consecutive, current_consecutive)


if __name__ == '__main__':
    s = Solution()

    assert s.longestConsecutive([100, 4, 200, 1, 3, 2]) == 4
    assert s.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
    assert s.longestConsecutive([1, 2, 0, 1]) == 3
