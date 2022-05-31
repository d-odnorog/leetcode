# https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/


class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        got = {s[i - k : i] for i in range(k, len(s) + 1)}
        return len(got) == 1 << k


class Solution2:
    def hasAllCodes(self, s: str, k: int) -> bool:
        need = 1 << k
        got = [False]*need
        all_one = need - 1
        hash_val = 0

        for i in range(len(s)):
            # calculate hash for s[i-k+1:i+1]
            hash_val = ((hash_val << 1) & all_one) | (int(s[i]))
            # hash only available when i-k+1 > 0
            if i >= k-1 and got[hash_val] is False:
                got[hash_val] = True
                need -= 1
                if need == 0:
                    return True
        return False


if __name__ == '__main__':
    for s in (Solution(), Solution2()):
        assert s.hasAllCodes('00110110', 2)
        assert s.hasAllCodes('0110', 1)
        assert not s.hasAllCodes('0110', 2)
