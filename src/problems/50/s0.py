class Solution:
    def myPow(self, x: float, n: int) -> float:
        return myPow1(x, n)


def myPow1(x: float, n: int) -> float:
    if n == 0:
        return 1
    if n == 1:
        return x
    if n % 2 == 0:
        res = myPow1(x, n // 2)
        return res * res
    else:
        res = myPow1(x, (n - 1) // 2)
        return res * res * x


def main():
    print(Solution().myPow(2, 10))
    print(Solution().myPow(2.1, 3))


main()
