# https://leetcode.com/problems/combination-sum-iii/


class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        result = [[0]]
        for i in reversed(range(k)):
            level = []
            for r in result:
                total = r.pop()

                start = r[-1] if r else 0

                for j in range(start + 1, 10):
                    res = r + [j]
                    if total + j * (i + 1) > n:
                        break
                    elif i == 0:
                        if total + j == n:
                            level.append(res)
                    else:
                        res.append(total + j)
                        level.append(res)

            result = level

        return result


if __name__ == '__main__':
    s = Solution()

    assert s.combinationSum3(3, 7) == [[1, 2, 4]]
    assert s.combinationSum3(3, 9) == [[1, 2, 6], [1, 3, 5], [2, 3, 4]]
    assert s.combinationSum3(4, 1) == []
