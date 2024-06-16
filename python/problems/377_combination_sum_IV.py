# https://leetcode.com/problems/combination-sum-iv/


class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        dp = [0] * (target + 1)

        dp[0] = 1

        for i in range(1, target + 1):
            for num in nums:
                num_before = i - num
                if num_before >= 0:
                    dp[i] += dp[num_before]

        return dp[target]


if __name__ == '__main__':
    s = Solution()

    assert s.combinationSum4([1, 2, 3], 4)
    assert s.combinationSum4([9], 3) == 0
