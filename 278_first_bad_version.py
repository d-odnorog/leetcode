# https://leetcode.com/problems/first-bad-version/
bad = 4


def isBadVersion(version: int) -> bool:
    return version >= bad


class Solution:
    def firstBadVersion(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2 if not isBadVersion(1) else 1
        elif isBadVersion(n) and not isBadVersion(n - 1):
            return n

        first, last = 0, n

        while True:
            version = first + (last - first) // 2
            if isBadVersion(version) and not isBadVersion(version - 1):  # to exit
                break
            elif isBadVersion(version):
                last = version
            else:
                first = version

        return version


class Solution2:
    def firstBadVersion(self, n: int) -> int:
        start = 1
        end = n
        while start < end:
            pivot = (start + end) // 2
            if isBadVersion(pivot):
                end = pivot
            else:
                start = pivot + 1

        return start


if __name__ == '__main__':
    s = Solution()

    assert s.firstBadVersion(5) == 4

    s2 = Solution2()

    assert s2.firstBadVersion(5) == 4
