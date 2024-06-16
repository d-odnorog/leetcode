# https://leetcode.com/problems/132-pattern/


class Solution:
    def find132pattern(self, nums: list[int]) -> bool:
        if len(nums) < 3:
            return False

        second_number = float('-inf')
        stack = []
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < second_number:
                return True
            while stack and stack[-1] < nums[i]:
                second_number = stack.pop()

            stack.append(nums[i])

        return False


if __name__ == '__main__':
    s = Solution()

    assert not s.find132pattern([1, 2, 3, 4])
    assert s.find132pattern([3, 1, 4, 2])
    assert s.find132pattern([-1, 3, 2, 0])
