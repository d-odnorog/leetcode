# https://leetcode.com/problems/two-sum/


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        length = len(nums)
        for i in range(length):
            for j in range(i, length):
                if i == j:
                    continue
                if nums[i] + nums[j] == target:
                    return [i, j]
        return [0]


class Solution2:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i, value in enumerate(nums):
            remaining = target - nums[i]

            if remaining in seen:
                return [seen[remaining], i]

            seen[value] = i


if __name__ == "__main__":
    s = Solution()
    assert s.twoSum([3, 2, 4], 6) == [1, 2]

    s2 = Solution2()
    assert s2.twoSum([3, 2, 4], 6) == [1, 2]
