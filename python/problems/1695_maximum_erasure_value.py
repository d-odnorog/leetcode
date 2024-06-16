# https://leetcode.com/problems/maximum-erasure-value/


class Solution:
    def maximumUniqueSubarray(self, nums: list[int]) -> int:
        seen = set()  # track visited elements in the window
        res = i = tot = 0
        for j in range(len(nums)):
            x = nums[j]
            # adjust the left bound of sliding window until you get all unique elements
            while i < j and x in seen:
                seen.remove(nums[i])
                tot -= nums[i]
                i += 1
            tot += x
            seen.add(x)
            res = max(res, tot)
        return res


if __name__ == '__main__':
    s = Solution()

    assert s.maximumUniqueSubarray([4, 2, 4, 5, 6]) == 17
    assert s.maximumUniqueSubarray([5, 2, 1, 2, 5, 2, 1, 2, 5]) == 8
