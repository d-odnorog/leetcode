# https://leetcode.com/problems/delete-operation-for-two-strings/
from functools import lru_cache


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        @lru_cache
        def lcs(i, j):  # find longest common subsequence
            if i == m or j == n:
                return 0
            return (
                1 + lcs(i + 1, j + 1)
                if word1[i] == word2[j]
                else max(lcs(i + 1, j), lcs(i, j + 1))
            )
        # subtract the lcs length from both the strings
        # the difference is the number of characters that has to deleted
        return m + n - 2 * lcs(0, 0)


class Solution2:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) > len(word2):
            word2, word1 = word1, word2

        m, n = len(word1), len(word2)
        prev = [0] * (m + 1)

        for i in range(n - 1, -1, -1):
            curr = [0] * (m + 1)
            for j in range(m - 1, -1, -1):
                if word1[j] == word2[i]:
                    curr[j] = 1 + prev[j + 1]
                else:
                    curr[j] = max(curr[j + 1], prev[j])
            prev = curr
        return m + n - 2 * prev[0]


if __name__ == '__main__':
    for s in (Solution(), Solution2()):
        assert s.minDistance('sea', 'eat') == 2
        assert s.minDistance('leetcode', 'etco') == 4
