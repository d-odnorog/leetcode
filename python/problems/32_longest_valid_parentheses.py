# https://leetcode.com/problems/longest-valid-parentheses/


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        max_len = 0
        last_unmatched_end = -1

        for i, p in enumerate(s):
            if p == '(':
                stack.append(i)
            else:
                if stack:
                    stack.pop()
                    if stack:
                        last_unmatched_open = stack[-1]
                        max_len = max(max_len, i - last_unmatched_open)
                    else:
                        max_len = max(max_len, i - last_unmatched_end)
                else:
                    last_unmatched_end = i
        return max_len


class Solution2:
    def longestValidParentheses(self, s: str) -> int:
        max_length = 0

        l, r = 0, 0
        # traverse the string from left to right
        for i in range(len(s)):
            if s[i] == '(':
                l += 1
            else:
                r += 1
            if l == r:  # valid balanced parantheses substring
                max_length = max(max_length, l * 2)
            elif r > l:  # invalid case as ')' is more
                l = r = 0

        l, r = 0, 0
        # traverse the string from right to left
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '(':
                l += 1
            else:
                r += 1
            if l == r:  # valid balanced parantheses substring
                max_length = max(max_length, l * 2)
            elif l > r:  # invalid case as '(' is more
                l = r = 0
        return max_length


if __name__ == '__main__':
    for s in (Solution(), Solution()):
        assert s.longestValidParentheses("(()") == 2
        assert s.longestValidParentheses(")()())") == 4
