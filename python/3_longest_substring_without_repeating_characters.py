# https://leetcode.com/problems/longest-substring-without-repeating-characters/
from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counter = defaultdict(int)  # track counts of each character
        l = 0
        max_length = 0
        for r, c in enumerate(s):
            counter[c] += 1
            if counter[c] > 1:
                while l < r and counter[c] > 1:  # iterate until window is valid
                    counter[s[l]] -= 1
                    l += 1
            max_length = max(max_length, r - l + 1)
        return max_length


class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        l = 0
        max_length = 0
        for r in range(len(s)):
            if s[r] in last_seen:
                l = max(last_seen[s[r]], l)

            last_seen[s[r]] = r + 1
            max_length = max(max_length, r - l + 1)
        return max_length


if __name__ == '__main__':
    for s in (Solution(), Solution2()):
        assert s.lengthOfLongestSubstring('abcabcbb') == 3
        assert s.lengthOfLongestSubstring('bbbbb') == 1
        assert s.lengthOfLongestSubstring('pwwkew') == 3
