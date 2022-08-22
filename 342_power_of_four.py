# https://leetcode.com/problems/power-of-four/
from math import sqrt, log


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return not (n & (n - 1)) and n & 1431655765 == n > 0


class Solution2:
    def isPowerOfFour(self, n: int) -> bool:
        return not (n & (n - 1)) and int(sqrt(n)) * int(sqrt(n)) == n > 0


class Solution3:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and log(n, 4).is_integer()


class Solution4:
    POWERS = {4**n for n in range(16)}

    def isPowerOfFour(self, n: int) -> bool:
        return n in self.POWERS


if __name__ == '__main__':
    for s in (Solution(), Solution2(), Solution3(), Solution4()):
        assert s.isPowerOfFour(16)
        assert not s.isPowerOfFour(5)
        assert s.isPowerOfFour(1)
        assert not s.isPowerOfFour(-2147483648)
        assert not s.isPowerOfFour(0)
        assert not s.isPowerOfFour(8)
