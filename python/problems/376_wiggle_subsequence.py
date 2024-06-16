# https://leetcode.com/problems/wiggle-subsequence/


class Solution:
    def wiggleMaxLength(self, nums: list[int]) -> int:
        f = 1
        d = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                f = d + 1
            elif nums[i] < nums[i - 1]:
                d = f + 1
        res = max(f, d)
        return res


if __name__ == '__main__':
    s = Solution()

    assert s.wiggleMaxLength([1, 7, 4, 9, 2, 5]) == 6
    assert s.wiggleMaxLength([1, 17, 5, 10, 13, 15, 10, 5, 16, 8]) == 7
    assert s.wiggleMaxLength([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 2
