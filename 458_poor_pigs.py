# https://leetcode.com/problems/poor-pigs/
from math import ceil, log2


class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        tmp = log2(buckets)  # number of pigs for one shot
        t = ceil(minutesToTest / minutesToDie)  # number of tests we can conduct

        if t == 1:
            return ceil(tmp)  # one shot is the answer

        # re-use pigs until the answer is found (# of tests)
        return ceil(tmp / log2(t + 1))


if __name__ == '__main__':
    s = Solution()

    assert s.poorPigs(1000, 15, 60) == 5
    assert s.poorPigs(4, 15, 15) == 2
    assert s.poorPigs(4, 15, 30) == 2
