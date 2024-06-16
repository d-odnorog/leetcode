# https://leetcode.com/problems/find-and-replace-pattern/
from collections import defaultdict


class Solution:
    @staticmethod
    def find(word):
        """Function that's calculate the numeric pattern."""
        l = []
        m = defaultdict(int)
        i = 0
        for c in word:
            if c in m:
                l.append(m[c])
            else:
                i += 1
                m[c] = i
                l.append(m[c])
        return l

    def findAndReplacePattern(self, words: list[str], pattern: str) -> list[str]:
        ans = []

        pfind = self.find(pattern)

        for w in words:
            wfind = self.find(w)

            # check if numeric pattern of pattern is equal to pattern of word
            if wfind == pfind:
                ans.append(w)

        return ans


if __name__ == '__main__':
    s = Solution()

    assert s.findAndReplacePattern(
        ['abc', 'deq', 'mee', 'aqq', 'dkd', 'ccc'], 'abb'
    ) == ['mee', 'aqq']
    assert s.findAndReplacePattern(['a', 'b', 'c'], 'a') == ['a', 'b', 'c']
