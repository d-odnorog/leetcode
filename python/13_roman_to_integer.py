# https://leetcode.com/problems/roman-to-integer/


class Solution:
    ROMAN_TO_INT = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    def romanToInt(self, s: str) -> int:
        prev = ''
        total = 0

        for letter in s:
            if prev == 'I' and letter == 'V':
                total -= 1
                number = 4
            elif prev == 'I' and letter == 'X':
                total -= 1
                number = 9
            elif prev == 'X' and letter == 'L':
                total -= 10
                number = 40
            elif prev == 'X' and letter == 'C':
                total -= 10
                number = 90
            elif prev == 'C' and letter == 'D':
                total -= 100
                number = 400
            elif prev == 'C' and letter == 'M':
                total -= 100
                number = 900
            else:
                number = self.ROMAN_TO_INT.get(letter)

            total += number
            prev = letter

        return total


if __name__ == '__main__':
    s = Solution()
    assert s.romanToInt('XII') == 12
    assert s.romanToInt('IX') == 9
    assert s.romanToInt('LVIII') == 58
    assert s.romanToInt('MCMXCIV') == 1994
