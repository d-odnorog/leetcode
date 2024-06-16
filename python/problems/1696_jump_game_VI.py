# https://leetcode.com/problems/jump-game-vi/
from collections import deque


class Solution:
    def maxResult(self, nums: list[int], k: int) -> int:
        dp = deque([(nums[0], 0)])

        for i in range(1, len(nums)):
            while dp and dp[0][1] + k < i:
                dp.popleft()

            cost = nums[i] + dp[0][0]

            while dp and cost >= dp[-1][0]:
                dp.pop()

            dp.append((cost, i))

        return dp[-1][0]


if __name__ == '__main__':
    s = Solution()

    assert s.maxResult([1, -1, -2, 4, -7, 3], 2) == 7
    assert s.maxResult([10, -5, -2, 4, 0, 3], 3) == 17
    assert s.maxResult([1, -5, -20, 4, -1, 3, -6, -3], 2) == 0
