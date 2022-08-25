# https://leetcode.com/problems/ransom-note/
from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        st = {}
        for letter in magazine:
            st[letter] = st.get(letter, 0) + 1

        for letter in ransomNote:
            if not st.get(letter):
                return False

            st[letter] = st[letter] - 1

            if st[letter] < 0:
                return False

        return True


class Solution2:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rn = Counter(ransomNote)
        mg = Counter(magazine)

        for k, v in rn.items():
            if k not in mg or mg[k] < v:
                return False

        return True


class Solution3:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for c in ransomNote:
            if c not in magazine:
                return False
            magazine = magazine.replace(c, '', 1)
        return True


if __name__ == '__main__':
    for s in (Solution(), Solution2(), Solution3()):
        assert not s.canConstruct('a', 'b')
        assert not s.canConstruct('aa', 'ab')
        assert s.canConstruct('aa', 'aab')
