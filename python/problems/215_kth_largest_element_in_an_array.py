# https://leetcode.com/problems/kth-largest-element-in-an-array/


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        nums.sort(reverse=True)

        n = nums[0]
        for i in range(k):
            if i == k:
                break
            else:
                n = nums[i]
                i += 1

        return n


class Solution2:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        return sorted(nums)[-k]


if __name__ == '__main__':
    for s in (Solution(), Solution2()):
        assert s.findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5
        assert s.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
