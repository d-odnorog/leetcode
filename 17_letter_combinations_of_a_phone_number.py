# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        DIGITS_TO_LETTERS = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        if len(digits) == 0:
            return []

        result = ['']
        for digit in digits:
            temporary = []
            for combo in result:
                for letter in DIGITS_TO_LETTERS[digit]:
                    temporary.append(combo + letter)
            result = temporary

        return result


if __name__ == '__main__':
    s = Solution()

    assert s.letterCombinations('23') == [
        'ad',
        'ae',
        'af',
        'bd',
        'be',
        'bf',
        'cd',
        'ce',
        'cf',
    ]
    assert s.letterCombinations('') == []
    assert s.letterCombinations('2') == ['a', 'b', 'c']
