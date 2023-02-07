# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []  # [[letter, duplicates]]

        for letter in s:
            if stack and stack[-1][0] == letter:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    _ = stack.pop()
            else:
                stack.append([letter, 1])

        return ''.join(letter * duplicates for letter, duplicates in stack)


if __name__ == '__main__':
    s = Solution()

    assert s.removeDuplicates('abcd', 2) == 'abcd'
    assert s.removeDuplicates('deeedbbcccbdaa', 3) == 'aa'
