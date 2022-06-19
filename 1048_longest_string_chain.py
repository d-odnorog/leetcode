# https://leetcode.com/problems/longest-string-chain/
from typing import List


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp = {}
        result = 1
        for word in sorted(words, key=len):
            dp[word] = 1
            for i in range(len(word)):
                prev = word[:i] + word[i + 1 :]
                if prev in dp:
                    dp[word] = dp[prev] + 1
                    result = max(result, dp[word])

        return result


if __name__ == '__main__':
    s = Solution()

    assert s.longestStrChain(['a', 'b', 'ba', 'bca', 'bda', 'bdca']) == 4
    assert s.longestStrChain(['xbc', 'pcxbcf', 'xb', 'cxbc', 'pcxbc']) == 5
