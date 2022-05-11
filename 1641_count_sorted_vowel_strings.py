# https://leetcode.com/problems/count-sorted-vowel-strings/


class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [1] * 5

        for _ in range(1, n):
            for i in range(1, 5):
                dp[i] = dp[i] + dp[i - 1]

        return sum(dp)


class Solution2:  # if you are really good at math :)
    def countVowelStrings(self, n: int) -> int:
        return ((n + 4) * (n + 3) * (n + 2) * (n + 1)) // 24


if __name__ == '__main__':
    for s in (Solution(), Solution2()):
        assert s.countVowelStrings(1) == 5
        assert s.countVowelStrings(2) == 15
        assert s.countVowelStrings(33) == 66045
