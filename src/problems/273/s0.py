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

        res = numberToWordsParsed(billions, millions, thousands, firsts)
        if res == "":
            return "Zero"
        return res


def numberToWordsParsed(b, m, t, f) -> str:
    if b == 0:
        if m == 0:
            if t == 0:
                return under1000ToWords(f)
            else:
                res = under1000ToWords(t)
                res2 = under1000ToWords(f)
                if res2 == "":
                    return res + " " + thousand
                return res + " " + thousand + " " + res2
        else:
            res = under1000ToWords(m)
            res2 = numberToWordsParsed(0, 0, t, f)
            if res2 == "":
                return res + " " + million
            return res + " " + million + " " + res2
    else:
        res = under1000ToWords(b)
        res2 = numberToWordsParsed(0, m, t, f)

        if res2 == "":
            return res + " " + billion
        return (
            under1000ToWords(b) + " " + billion + " " + numberToWordsParsed(0, m, t, f)
        )


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


def under1000ToWords(num: int) -> str:
    # numcpy = num
    first = num % 10
    num //= 10
    tens = num % 10
    num //= 10
    hundreds = num % 10

    return under1000ToWordsParsed(hundreds, tens, first)


def under1000ToWordsParsed(h: int, t: int, f: int) -> str:
    if h == 0:
        if t == 0:
            if f == 0:
                return ""
            return ut[f]
        elif t == 1:
            return utwenty[f]
        else:
            res2 = under1000ToWordsParsed(0, 0, f)
            if res2 == "":
                return uh[t]
            return uh[t] + " " + res2
    else:
        res2 = under1000ToWordsParsed(0, t, f)
        if res2 == "":
            return ut[h] + " " + hundred
        return ut[h] + " " + hundred + " " + res2


def main():
    print(Solution().numberToWords(123))
    print(Solution().numberToWords(12345))
    print(Solution().numberToWords(1234567))
    print("|" + Solution().numberToWords(20) + "|")


if __name__ == "__main__":
    main()
