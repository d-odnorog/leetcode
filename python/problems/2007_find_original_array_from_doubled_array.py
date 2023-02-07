# https://leetcode.com/problems/find-original-array-from-doubled-array/
from collections import Counter
from typing import List


class Solution:
    def findOriginalArray(self, nums: List[int]) -> List[int]:
        answer = []
        vacant = []

        if len(nums) % 2:
            return answer

        nums.sort()

        temp = Counter(nums)

        for i in nums:
            if temp[i] == 0:
                # if we have already decreased it's value when we were checking y/2 value,
                # like 2,4 we will remove 4 also when we will check 2
                # but our iteration will come again on 4.
                continue
            else:
                if temp.get(2 * i, 0) >= 1:
                    # if we have both y and y*2, store in our ans array
                    answer.append(i)
                    # decrease the frequency of y and y*2
                    temp[2 * i] -= 1
                    temp[i] -= 1
                else:
                    return vacant

        return answer


if __name__ == '__main__':
    s = Solution()

    assert s.findOriginalArray([1, 3, 4, 2, 6, 8]) == [1, 3, 4]
    assert s.findOriginalArray([6, 3, 0, 1]) == []
    assert s.findOriginalArray([1]) == []
