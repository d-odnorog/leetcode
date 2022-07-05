# https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/
from typing import List


class Solution:
    def maxArea(
        self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]
    ) -> int:
        horizontalCuts.append(0)
        horizontalCuts.append(h)

        verticalCuts.append(0)
        verticalCuts.append(w)

        l, b = 0, 0

        horizontalCuts.sort()
        verticalCuts.sort()

        for i in range(1, len(horizontalCuts)):
            b = max(b, horizontalCuts[i] - horizontalCuts[i - 1])

        for j in range(1, len(verticalCuts)):
            l = max(l, verticalCuts[j] - verticalCuts[j - 1])

        return (l * b) % (10**9 + 7)


if __name__ == '__main__':
    s = Solution()

    assert s.maxArea(h=5, w=4, horizontalCuts=[1, 2, 4], verticalCuts=[1, 3]) == 4
    assert s.maxArea(h=5, w=4, horizontalCuts=[3, 1], verticalCuts=[1]) == 6
    assert s.maxArea(h=5, w=4, horizontalCuts=[3], verticalCuts=[3]) == 9
