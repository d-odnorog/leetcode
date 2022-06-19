# https://leetcode.com/problems/palindrome-number/


class Solution:
    def isPalindrome(self, x: int) -> bool:
        string = str(x)
        for i in range(int(len(string) / 2)):
            if string[i] != string[-i - 1]:
                return False

        return True


class Solution2:
    def isPalindrome(self, x: int) -> bool:
        string = str(x)
        return False if string != string[::-1] else True


class Solution3:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x > 0 and x % 10 == 0):
            return False

        reversed_num = 0
        while x > reversed_num:
            reversed_num = reversed_num * 10 + x % 10
            x = x // 10

        return True if (x == reversed_num or x == reversed_num // 10) else False


if __name__ == '__main__':
    s = Solution()
    assert s.isPalindrome(12221)
    assert not s.isPalindrome(122222)

    s2 = Solution2()
    assert s2.isPalindrome(12221)
    assert not s2.isPalindrome(122222)

    s3 = Solution3()
    assert s3.isPalindrome(12221)
    assert not s3.isPalindrome(1223455)
