from typing import List


class Solution:
    def fib(self, n: int) -> int:
        return fib(n)


def fib(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1

    cache1 = 0
    cache2 = 1
    for _ in range(2, n):
        tmp = cache1 + cache2
        cache1 = cache2
        cache2 = tmp

    return cache1 + cache2


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
    (40, 102334155),
    (50, 12586269025),
]

for input, output in data:
    print(Solution().fib(input), output)
