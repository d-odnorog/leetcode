# https://leetcode.com/problems/first-unique-character-in-a-string/


class Solution:
    def firstUniqChar(self, s: str) -> int:
        storage = dict()

        for letter in s:
            storage[letter] = storage.get(letter, 0) + 1

        for i, letter in enumerate(s):
            if storage[letter] == 1:
                return i

        return -1


if __name__ == '__main__':
    s = Solution()

    assert s.firstUniqChar('leetcode') == 0
    assert s.firstUniqChar('loveleetcode') == 2
    assert s.firstUniqChar('aabb') == -1
