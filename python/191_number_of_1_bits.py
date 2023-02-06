# https://leetcode.com/problems/number-of-1-bits/


class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        while n:
            cnt += 1
            n = n & (n - 1)
        return cnt


class Solution2:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')


if __name__ == '__main__':
    for s in (Solution(), Solution2()):
        assert s.hammingWeight(0o00000000000000000000000000001011) == 3
        assert s.hammingWeight(0o00000000000000000000000010000000) == 1
        assert s.hammingWeight(0o11111111111111111111111111111101) == 31
