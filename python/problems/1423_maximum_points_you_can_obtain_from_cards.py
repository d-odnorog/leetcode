# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/


class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        n = len(cardPoints)
        total = sum(cardPoints)

        remaining_length = n - k
        subarray_sum = sum(cardPoints[:remaining_length])

        min_sum = subarray_sum
        for i in range(remaining_length, n):
            # Update the sliding window sum to the subarray ending at index i
            subarray_sum += cardPoints[i]
            subarray_sum -= cardPoints[i - remaining_length]
            # Update min_sum to track the overall minimum sum so far
            min_sum = min(min_sum, subarray_sum)
        return total - min_sum


if __name__ == '__main__':
    s = Solution()

    assert s.maxScore([1, 2, 3, 4, 5, 6, 1], 3) == 12
    assert s.maxScore([2, 2, 2], 2) == 4
    assert s.maxScore([9, 7, 7, 9, 7, 7, 9], 7) == 55
