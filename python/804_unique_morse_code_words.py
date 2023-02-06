# https://leetcode.com/problems/unique-morse-code-words/
from typing import List


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = {
            'a': '.-',
            'b': '-...',
            'c': '-.-.',
            'd': '-..',
            'e': '.',
            'f': '..-.',
            'g': '--.',
            'h': '....',
            'i': '..',
            'j': '.---',
            'k': '-.-',
            'l': '.-..',
            'm': '--',
            'n': '-.',
            'o': '---',
            'p': '.--.',
            'q': '--.-',
            'r': '.-.',
            's': '...',
            't': '-',
            'u': '..-',
            'v': '...-',
            'w': '.--',
            'x': '-..-',
            'y': '-.--',
            'z': '--..',
        }

        st = set()
        for word in words:
            encoded_word = ''
            for letter in word:
                encoded_word += morse[letter]
            st.add(encoded_word)

        return len(st)


class Solution2(object):
    def uniqueMorseRepresentations(self, words):
        MORSE = [
            '.-',
            '-...',
            '-.-.',
            '-..',
            '.',
            '..-.',
            '--.',
            '....',
            '..',
            '.---',
            '-.-',
            '.-..',
            '--',
            '-.',
            '---',
            '.--.',
            '--.-',
            '.-.',
            '...',
            '-',
            '..-',
            '...-',
            '.--',
            '-..-',
            '-.--',
            '--..',
        ]

        seen = {''.join(MORSE[ord(c) - ord('a')] for c in word) for word in words}

        return len(seen)


if __name__ == '__main__':
    for s in (Solution(), Solution2()):
        assert s.uniqueMorseRepresentations(['gin', 'zen', 'gig', 'msg']) == 2
        assert s.uniqueMorseRepresentations(['a']) == 1
