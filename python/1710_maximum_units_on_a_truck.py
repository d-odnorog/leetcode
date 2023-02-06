# https://leetcode.com/problems/maximum-units-on-a-truck/
from typing import List


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # Sort boxes so that boxes with the most units appear first
        boxTypes.sort(key=lambda box: box[1], reverse=True)

        total_units = 0
        for number_of_boxes, units_per_box in boxTypes:
            # Take as many boxes until we're out of space on the truck
            # or we're out of boxes of this type
            num_boxes = min(truckSize, number_of_boxes)
            total_units += num_boxes * units_per_box
            truckSize -= num_boxes

        return total_units


if __name__ == '__main__':
    s = Solution()

    assert s.maximumUnits([[1, 3], [2, 2], [3, 1]], 4) == 8
    assert s.maximumUnits([[5, 10], [2, 5], [4, 7], [3, 9]], 10) == 91
