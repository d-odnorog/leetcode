# https://leetcode.com/problems/sort-array-by-parity/
from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even_numbers, odd_numbers = [], []

        for n in nums:
            if n % 2:
                odd_numbers.append(n)
            else:
                even_numbers.append(n)

        return even_numbers + odd_numbers


class Solution2(object):
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        nums.sort(key=lambda x: x % 2)
        return nums


if __name__ == "__main__":
    s = Solution()
    assert s.sortArrayByParity([3, 1, 2, 4]) == [2, 4, 3, 1]

    s2 = Solution2()
    assert s2.sortArrayByParity([3, 1, 2, 4]) == [2, 4, 3, 1]
