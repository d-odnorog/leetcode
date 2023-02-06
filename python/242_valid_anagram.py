# https://leetcode.com/problems/valid-anagram/


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        h1, h2 = dict(), dict()

        for letter in s:
            h1[letter] = h1.get(letter, 0) + 1

        for letter in t:
            h2[letter] = h2.get(letter, 0) + 1

        if h1 == h2:
            return True

        return False


class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        flag = True
        if len(s) != len(t):
            flag = False
        else:
            letters = "abcdefghijklmnopqrstuvwxyz"
            for letter in letters:
                if s.count(letter) != t.count(letter):
                    flag = False
                    break

        return flag


if __name__ == '__main__':
    for s in (Solution(), Solution2()):
        assert s.isAnagram('anagram', 'nagaram')
        assert not s.isAnagram('rat', 'car')
