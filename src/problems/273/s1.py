from typing import List, Optional


class Solution:
    def numberToWords(self, num: int) -> str:
        firsts = num % 1000
        num //= 1000
        thousands = num % 1000
        num //= 1000
        millions = num % 1000
        num //= 1000
        billions = num % 1000

        acc = []
        numberToWordsParsed(billions, millions, thousands, firsts, acc)
        if len(acc) == 0:
            return "Zero"

        return " ".join(acc)


def numberToWordsParsed(b: int, m: int, t: int, f: int, acc: list[str]):
    if b == 0:
        if m == 0:
            if t == 0:
                under1000ToWords(f, acc)
            else:
                res = under1000ToWords(t, acc)
                acc.append(thousand)
                res2 = under1000ToWords(f, acc)
        else:
            res = under1000ToWords(m, acc)
            acc.append(million)
            res2 = numberToWordsParsed(0, 0, t, f, acc)
    else:
        res = under1000ToWords(b, acc)
        acc.append(billion)
        res2 = numberToWordsParsed(0, m, t, f, acc)


ut = [
    "Zero",
    "One",
    "Two",
    "Three",
    "Four",
    "Five",
    "Six",
    "Seven",
    "Eight",
    "Nine",
]

utwenty = [
    "Ten",
    "Eleven",
    "Twelve",
    "Thirteen",
    "Fourteen",
    "Fifteen",
    "Sixteen",
    "Seventeen",
    "Eighteen",
    "Nineteen",
]

uh = [
    "",
    "Ten",
    "Twenty",
    "Thirty",
    "Forty",
    "Fifty",
    "Sixty",
    "Seventy",
    "Eighty",
    "Ninety",
]

hundred = "Hundred"
thousand = "Thousand"
million = "Million"
billion = "Billion"


def under1000ToWords(num: int, acc: List[str]):
    first = num % 10
    num //= 10
    tens = num % 10
    num //= 10
    hundreds = num % 10

    under1000ToWordsParsed(hundreds, tens, first, acc)


def under1000ToWordsParsed(h: int, t: int, f: int, acc: List[str]):
    if h == 0:
        if t == 0:
            if f == 0:
                return
            return acc.append(ut[f])
        elif t == 1:
            return acc.append(utwenty[f])
        else:
            acc.append(uh[t])
            under1000ToWordsParsed(0, 0, f, acc)
    else:
        acc.append(ut[h])
        acc.append(hundred)
        under1000ToWordsParsed(0, t, f, acc)


def main():
    print(Solution().numberToWords(123))
    print(Solution().numberToWords(12345))
    print(Solution().numberToWords(1234567))
    print("|" + Solution().numberToWords(20) + "|")


if __name__ == "__main__":
    main()
