# https://leetcode.com/problems/divide-two-integers/


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = 1

        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            sign = -1
        if dividend < 0:
            dividend = dividend - dividend - dividend
        if divisor < 0:
            divisor = divisor - divisor - divisor

        if divisor == 1:
            return self._handle_result(sign * dividend)

        result = 0
        while dividend >= divisor:
            to_substract, quotient = self._compute_iteration(dividend, divisor)
            dividend -= to_substract
            result += quotient

        return self._handle_result(sign * result)

    @staticmethod
    def _handle_result(result: int) -> int:
        if result < pow(-2, 31):
            return pow(-2, 31)
        if result > pow(2, 31) - 1:
            return pow(2, 31) - 1
        return result

    @staticmethod
    def _compute_iteration(dividend, divisor) -> (int, int):
        dividend_str = str(dividend)
        divisor_str = str(divisor)
        number_of_zeros = len(dividend_str) - len(divisor_str)
        if int(dividend_str[0 : len(divisor_str)]) < divisor:
            number_of_zeros -= 1
        return (
            int(divisor_str + '0' * number_of_zeros),
            int('1' + '0' * number_of_zeros),
        )


if __name__ == '__main__':
    s = Solution()

    assert s.divide(10, 3) == 3
    assert s.divide(7, -3) == -2
