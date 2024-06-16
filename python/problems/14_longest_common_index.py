# https://leetcode.com/problems/longest-common-prefix/


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        strs.sort()

        prefix = ''
        for letter in strs[0]:
            if strs[-1].startswith(prefix + letter):
                prefix += letter
            else:
                break

        return prefix


class Solution2:
    def _hasCommonPrefix(self, middle: int, strs: list[str]) -> bool:
        prefix = strs[0][:middle]
        for word in strs:
            if not word.startswith(prefix):
                return False

        return True

    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        min_len = 201
        for word in strs:
            min_len = min(min_len, len(word))

        low = 1
        high = min_len
        while low <= high:
            middle = int((low + high) / 2)
            if self._hasCommonPrefix(middle, strs):
                low = middle + 1
            else:
                high = middle - 1

        middle = int((low + high) / 2)
        return strs[0][:middle]


if __name__ == '__main__':
    s = Solution()

    assert s.longestCommonPrefix(['flower', 'flow', 'flight']) == 'fl'
    assert not s.longestCommonPrefix(['dog', 'racecar', 'car'])
    assert s.longestCommonPrefix(['flower', 'flower', 'flower', 'flower']) == 'flower'
    assert s.longestCommonPrefix(['ab', 'a']) == 'a'

    s2 = Solution2()

    assert s2.longestCommonPrefix(['flower', 'flow', 'flight']) == 'fl'
    assert not s2.longestCommonPrefix(['dog', 'racecar', 'car'])
    assert s2.longestCommonPrefix(['flower', 'flower', 'flower', 'flower']) == 'flower'
    assert s2.longestCommonPrefix(['ab', 'a']) == 'a'
