# https://leetcode.com/problems/largest-perimeter-triangle/


class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        l = len(nums)
        nums.sort(reverse=True)

        for i in range(1, l - 1):
            if nums[i - 1] < nums[i] + nums[i + 1]:
                return sum(nums[i - 1 : i + 2])

        return 0


if __name__ == '__main__':
    s = Solution()

    assert s.largestPerimeter([2, 1, 2]) == 5
    assert s.largestPerimeter([1, 1, 2]) == 0
