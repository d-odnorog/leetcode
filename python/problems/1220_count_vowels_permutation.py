# https://leetcode.com/problems/count-vowels-permutation/
import math
from functools import lru_cache


class Solution:
    def countVowelPermutation(self, n: int) -> int:
        moduler = math.pow(10, 9) + 7
        a, e, i, o, u = [1] * 5
        for _ in range(n - 1):
            a, e, i, o, u = map(
                lambda x: x % moduler, [(e + i + u), (a + i), (e + o), (i), (i + o)]
            )
        return int((a + e + i + o + u) % moduler)


class Solution2:
    def countVowelPermutation(self, n: int) -> int:

        # A mapper mapped characters to their next characters
        mapper = {
            "": ["a", "e", "i", "o", "u"],
            "a": "e",
            "e": ["a", "i"],
            "i": ["a", "e", "o", "u"],
            "o": ["i", "u"],
            "u": ["a"],
        }

        @lru_cache(None)
        def dp(n, c):

            # If n == 1, we have reach base case and thus, return 1
            if n == 1:
                return 1

            # Initialize the total to 0
            total = 0

            # Recursively solve sub-problems until n is reduced to 1
            for char in mapper[c]:
                total = (total + dp(n - 1, char)) % 1000000007

            return total

        # Add 1 to n since we started with empty string instead of recursively called dp on each vowel
        return dp(n + 1, "")


if __name__ == '__main__':
    for s in (Solution(), Solution2()):
        assert s.countVowelPermutation(1) == 5
        assert s.countVowelPermutation(2) == 10
        assert s.countVowelPermutation(5) == 68
