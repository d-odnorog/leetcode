# https://leetcode.com/problems/trapping-rain-water/


class Solution:
    # Time Complexity: O(N)
    # Space Complexity: O(1)
    # two pointers
    # pointer i from the left
    # pointer j from the right

    def trap(self, height: list[int]) -> int:
        i, j, ans, ma, mi = 0, len(height) - 1, 0, 0, 0

        while i <= j:
            # take the min height
            mi = min(height[i], height[j])
            # find the max min height
            ma = max(ma, mi)

            # the units of water being tapped is the difference between max height and min height
            ans += ma - mi

            if height[i] < height[j]:
                # move the pointer i if height[i] is smaller
                i += 1
            else:
                # else move pointer j
                j -= 1

        return ans


if __name__ == '__main__':
    s = Solution()

    assert s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
    assert s.trap([4, 2, 0, 3, 2, 5]) == 9
