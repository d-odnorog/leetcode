# https://leetcode.com/problems/short-encoding-of-words/
from collections import Counter
from typing import List


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words = set(words)
        counter = Counter(word[i:] for word in words for i in range(len(word)))
        return sum(len(word) + 1 for word in words if counter[word] == 1)


if __name__ == '__main__':
    s = Solution()

    assert s.minimumLengthEncoding(['time', 'me', 'bell']) == 10
    assert s.minimumLengthEncoding(['t']) == 2
