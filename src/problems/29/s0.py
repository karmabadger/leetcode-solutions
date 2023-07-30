from typing import List, Tuple


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        return div(dividend, divisor)
        if dividend == 0 or divisor == 0:
            return 0

        if divisor == -1:
            if dividend == MIN_INT:
                return MAX_INT
            return -dividend

        if dividend == MIN_INT and divisor == -1:
            return MAX_INT

        if dividend < 0:
            if divisor < 0:
                return div(dividend, divisor)
            else:
                return -div(dividend, -divisor)
        else:
            if divisor > 0:
                return div(dividend, divisor)
            else:
                return -div(dividend, -divisor)


# must have same sign
def div(dividend: int, divisor: int) -> int:
    if abs(dividend) < abs(divisor):
        return 0

    if divisor == 1:
        return dividend

    divid = dividend
    divis = divisor

    total = 0
    while True:
        

    return res


MIN_INT = -2147483648
MAX_INT = 2147483647


def clamp(num: int) -> int:
    if num < MIN_INT:
        return MIN_INT
    elif num > MAX_INT:
        return MAX_INT
    else:
        return num


def count_sd(num: int) -> int:
    for i in range(32):
        if num >> i == 0:
            return i
    return -1


data = [
    ((10, 2), 5),
    # ((10, 3), 3),
    # ((-7, -3), -2),
]

for input, output in data:
    print(Solution().divide(input[0], input[1]), output)
