# https://leetcode.com/problems/merge-sorted-array/
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        tmp_nums1 = nums1[:m]

        p1, p2 = 0, 0

        for p in range(n + m):
            if p2 >= n or (p1 < m and tmp_nums1[p1] <= nums2[p2]):
                nums1[p] = tmp_nums1[p1]
                p1 += 1
            else:
                nums1[p] = nums2[p2]
                p2 += 1


class Solution2:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # start merging from the ends of the lists
        p1, p2 = m - 1, n - 1
        # destination d index to insert into nums1
        for d in range(m + n - 1, -1, -1):
            # if second list is empty, nothing more to merge
            if p2 < 0:
                return
            # only merge from nums1 if there are items left to merge
            # insert at d the larger of the two values from nums1 and nums2
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[d] = nums1[p1]
                p1 -= 1
            else:
                nums1[d] = nums2[p2]
                p2 -= 1


if __name__ == '__main__':
    for s in (Solution(), Solution2()):

        nums1, m, nums2, n = [1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3
        s.merge(nums1, m, nums2, n)
        assert nums1 == [1, 2, 2, 3, 5, 6]

        nums1, m, nums2, n = [1], 1, [], 0
        s.merge(nums1, m, nums2, n)
        assert nums1 == [1]

        nums1, m, nums2, n = [0], 0, [1], 1
        s.merge(nums1, m, nums2, n)
        assert nums1 == [1]
