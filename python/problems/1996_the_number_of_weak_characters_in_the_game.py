# https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/
from typing import List


class Solution:
    # the idea is to
    # 1. rearrange the order of attack and defense
    # 2. count weak characters (those defenses less than the current maximum defense)
    # 3. update the maximum defense
    def numberOfWeakCharacters(self, p: List[List[int]]) -> int:
        # the final answer to be returned
        weakCharacters = 0
        # record maximum defense. since 1 <= defense_i <= 10 ^ 5
        # we can set the init value to x where x < 1
        maxDefense = 0
        # sort properties with custom sort comparator
        # if the attack is same, then sort defense in descending order
        # otherwise, sort attack in in ascending order
        p.sort(key=lambda x: (x[0], -x[1]), reverse=True)
        # or we can do it like
        # p.sort(key = lambda x: (-x[0], x[1]))
        for _, defense in p:
            # if it is less than current maxDefense, then it means it is a weak character
            if defense < maxDefense:
                weakCharacters += 1
            # update maxDefense
            else:
                maxDefense = defense
        return weakCharacters


if __name__ == '__main__':
    s = Solution()

    assert s.numberOfWeakCharacters([[5, 5], [6, 3], [3, 6]]) == 0
    assert s.numberOfWeakCharacters([[2, 2], [3, 3]]) == 1
    assert s.numberOfWeakCharacters([[1, 5], [10, 4], [4, 3]]) == 1
