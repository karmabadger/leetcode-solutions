from typing import List


class Solution:
    def fib(self, n: int) -> int:
        return fib(n)


def fib(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1

    cache: List[int] = [0] * n
    cache[1] = 1
    for i in range(2, n):
        cache[i] = cache[i - 1] + cache[i - 2]

    return cache[n - 1] + cache[n - 2]


data = [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (10, 55),
    (20, 6755),
    (30, 6755),
    (35, 9227465),
    # (40, 102334155),
    # (50, 12586269025),
]

for input, output in data:
    print(Solution().fib(input), output)
