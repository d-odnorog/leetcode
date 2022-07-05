# https://leetcode.com/problems/candy/
from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        length = len(ratings)
        candies = [1] * length
        for i in range(1, length):
            if ratings[i] > ratings[i - 1] and candies[i] <= candies[i - 1]:
                candies[i] = candies[i - 1] + 1
        for i in range(length - 2, -1, -1):
            if ratings[i] > ratings[i + 1] and candies[i] <= candies[i + 1]:
                candies[i] = candies[i + 1] + 1
        return sum(candies)


if __name__ == '__main__':
    s = Solution()

    assert s.candy([1, 0, 2]) == 5
    assert s.candy([1, 2, 2]) == 4
