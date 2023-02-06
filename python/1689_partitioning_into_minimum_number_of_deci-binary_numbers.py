# https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/


class Solution:
    def minPartitions(self, n: str) -> int:
        return int(max(n))


if __name__ == '__main__':
    s = Solution()

    assert s.minPartitions('32') == 3
    assert s.minPartitions('82734') == 8
    assert s.minPartitions('27346209830709182346') == 9
