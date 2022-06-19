# https://leetcode.com/problems/median-of-two-sorted-arrays/
from typing import List


class Solution:
    def _find_i(self, a: List[int], b: List[int], i: int) -> int:
        m = len(a)
        n = len(b)

        # end case for recursion
        if m == 0:
            return b[i]
        if n == 0:
            return a[i]

        # choose pivot
        p = m // 2 + 1
        q = n // 2 + 1

        # handle case 1 and 2 (see explanation above)
        if a[p - 1] >= b[q - 1]:
            if i <= p + q - 2:
                return self._find_i(a[: p - 1], b, i)
            else:
                return self._find_i(a, b[q:], i - q)

        # handle case 3 and 4 (see explanation above)
        else:
            if i <= p + q - 2:
                return self._find_i(a, b[: q - 1], i)
            else:
                return self._find_i(a[p:], b, i - p)

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # use find_i to solve the find median problem
        l1 = len(nums1)
        l2 = len(nums2)
        if (l1 + l2) % 2 == 1:
            return self._find_i(nums1, nums2, (l1 + l2) // 2)
        else:
            return (
                self._find_i(nums1, nums2, (l1 + l2) // 2 - 1)
                + self._find_i(nums1, nums2, (l1 + l2) // 2)
            ) / 2


if __name__ == '__main__':
    s = Solution()

    assert s.findMedianSortedArrays([1, 3], [2]) == 2.0
    assert s.findMedianSortedArrays([1, 2], [3, 4]) == 2.5
