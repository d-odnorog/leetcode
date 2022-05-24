# https://leetcode.com/problems/ones-and-zeroes/
from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        counter = [[s.count("0"), s.count("1")] for s in strs]

        for zeroes, ones in counter:
            for i in range(m, zeroes - 1, -1):
                for j in range(n, ones - 1, -1):
                    dp[i][j] = max(dp[i][j], 1 + dp[i - zeroes][j - ones])

        return dp[-1][-1]


if __name__ == '__main__':
    s = Solution()

    assert s.findMaxForm(['10', '0001', '111001', '1', '0'], 5, 3) == 4
    assert s.findMaxForm(['10', '0', '1'], 1, 1) == 2
