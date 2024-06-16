# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/


class Solution:
    def findUnsortedSubarray(self, nums: list[int]) -> int:
        ma = -10001
        mi = 10001
        length = len(nums)

        if length == 1:
            return 0
        elif length == 2:
            return 0 if nums[0] <= nums[1] else 2

        for i in range(1, length):
            if nums[i] <= nums[i - 1]:
                mi = min(mi, nums[i])

        if mi == 10001:
            return 0

        for i in range(length - 2, -1, -1):
            if nums[i] > nums[i + 1]:
                ma = max(ma, nums[i])

        left = 0
        for i in range(0, length):
            left = i
            if mi < nums[left]:
                break

        right = 0
        for i in range(length - 1, -1, -1):
            right = i
            if ma > nums[right]:
                break

        return right - left + 1


class Solution2:
    def findUnsortedSubarray(self, nums: list[int]) -> int:
        if len(nums) < 2:
            return 0

        start, end = -1, 0
        left_prev, right_prev = nums[0], nums[start]

        for i in range(1, len(nums)):
            # find the largest index not in place
            if nums[i] < left_prev:
                end = i
            else:
                left_prev = nums[i]

            # find the smallest index not in place
            if right_prev < nums[~i]:
                start = ~i
            else:
                right_prev = nums[~i]

        if end != 0:
            return end - (len(nums) + start) + 1
        else:
            return 0


if __name__ == '__main__':
    s = Solution()

    assert s.findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]) == 5
    assert not s.findUnsortedSubarray([1, 2, 3, 4])
    assert not s.findUnsortedSubarray([1])
    assert s.findUnsortedSubarray([5, 4, 3, 2, 1]) == 5
    assert s.findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]) == 5
    assert not s.findUnsortedSubarray([1, 1])

    s2 = Solution2()

    assert s2.findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]) == 5
    assert not s2.findUnsortedSubarray([1, 2, 3, 4])
    assert not s2.findUnsortedSubarray([1])
    assert s2.findUnsortedSubarray([5, 4, 3, 2, 1]) == 5
    assert s2.findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]) == 5
    assert not s2.findUnsortedSubarray([1, 1])
