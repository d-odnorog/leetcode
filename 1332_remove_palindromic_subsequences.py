# https://leetcode.com/problems/remove-palindromic-subsequences/


class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if s == s[::-1]:
            return 1

        return 2


if __name__ == '__main__':
    s = Solution()

    assert s.removePalindromeSub('ababa') == 1
    assert s.removePalindromeSub('abb') == 2
    assert s.removePalindromeSub('baabb') == 2
