# https://leetcode.com/problems/max-number-of-k-sum-pairs/
from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        table = {}  # {number: amount}
        operations = 0
        for i in nums:
            if k - i in table and table[k - i] > 0:
                operations += 1
                table[k - i] -= 1
            else:
                table[i] = table.get(i, 0) + 1

        return operations


if __name__ == '__main__':
    s = Solution()

    assert s.maxOperations([1, 2, 3, 4], 5) == 2
    assert s.maxOperations([3, 1, 3, 4, 3], 6) == 1
