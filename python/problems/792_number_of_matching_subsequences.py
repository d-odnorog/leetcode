# https://leetcode.com/problems/number-of-matching-subsequences/


class Solution:
    def numMatchingSubseq(self, s: str, words: list[str]) -> int:
        def is_subsequence(s1, s2):

            i = j = 0

            while i < len(s1) and j < len(s2):
                if s1[i] == s2[j]:
                    i += 1
                j += 1
            return len(s1) == i

        cache = {}
        count = 0

        for word in words:
            if word not in cache:
                if is_subsequence(word, s):
                    count += 1
                    cache[word] = True
                else:
                    cache[word] = False
            else:
                if cache[word]:
                    count += 1

        return count


if __name__ == '__main__':
    s = Solution()

    assert s.numMatchingSubseq("abcde", ["a", "bb", "acd", "ace"]) == 3
    assert (
        s.numMatchingSubseq("dsahjpjauf", ["ahjpjau", "ja", "ahbwzgqnuk", "tnmlanowax"])
        == 2
    )
