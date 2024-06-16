# https://leetcode.com/problems/backspace-string-compare/


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        clean_s, clean_t = [], []

        for letter in s:
            if letter == '#' and clean_s:
                clean_s.pop()
            elif letter != '#':
                clean_s.append(letter)

        for letter in t:
            if letter == '#' and clean_t:
                clean_t.pop()
            elif letter != '#':
                clean_t.append(letter)

        return True if clean_s == clean_t else False


class Solution2:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(string: str) -> list[str]:
            result = []
            for letter in string:
                if letter != '#':
                    result.append(letter)
                elif result:
                    result.pop()
            return result

        return build(s) == build(t)


if __name__ == '__main__':
    s = Solution()

    assert s.backspaceCompare('ab#c', 'ad#c')
    assert s.backspaceCompare('ab##', 'c#d#')
    assert not s.backspaceCompare('a#c', 'b')
    assert s.backspaceCompare('y#fo##f', 'y#f#o##f')

    s2 = Solution2()

    assert s2.backspaceCompare('ab#c', 'ad#c')
    assert s2.backspaceCompare('ab##', 'c#d#')
    assert not s2.backspaceCompare('a#c', 'b')
    assert s2.backspaceCompare('y#fo##f', 'y#f#o##f')
