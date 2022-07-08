# https://leetcode.com/problems/fibonacci-number/


class Solution:
    def fib(self, n: int) -> int:
        if n in [0, 1]:
            return n
        else:
            return self.fib(n-1) + self.fib(n-2)


class Solution2:
    def fib(self, n: int) -> int:
        dp = [0, 1]

        for i in range(2, n + 1):
            dp.append(dp[i - 1] + dp[i - 2])

        return dp[n]


if __name__ == '__main__':
    for s in (Solution(), Solution2()):
        assert s.fib(2) == 1
        assert s.fib(3) == 2
        assert s.fib(4) == 3
