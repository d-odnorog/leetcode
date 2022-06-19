# https://leetcode.com/problems/fizz-buzz/
from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for i in range(1, n + 1):
            if not i % 15:
                result.append('FizzBuzz')
            elif not i % 3:
                result.append('Fizz')
            elif not i % 5:
                result.append('Buzz')
            else:
                result.append(str(i))

        return result


if __name__ == '__main__':
    s = Solution()
    assert s.fizzBuzz(15) == [
        "1",
        "2",
        "Fizz",
        "4",
        "Buzz",
        "Fizz",
        "7",
        "8",
        "Fizz",
        "Buzz",
        "11",
        "Fizz",
        "13",
        "14",
        "FizzBuzz",
    ]
