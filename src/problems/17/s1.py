from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)

        if n == 0:
            return []
        elif n == 1:
            i = ord(digits[0]) - 48
            poss1 = digits_to_letters[i]
            return list(poss1)
        else:
            return gen_list(digits, 0, "")


def gen_list(digits: str, index: int, acc: str) -> List[str]:
    if len(digits) == index:
        return ["".join(acc)]
    else:
        res = []
        for c in digits_to_letters[ord(digits[index]) - 48]:
            res.extend(gen_list(digits, index + 1, acc + c))
        return res


digits_to_letters = [
    "",
    "",
    "abc",
    "def",
    "ghi",
    "jkl",
    "mno",
    "pqrs",
    "tuv",
    "wxyz",
]


def main():
    print(Solution().letterCombinations("23"))
    print(Solution().letterCombinations(""))
    print(Solution().letterCombinations("2"))
    print(Solution().letterCombinations("234"))
    print(Solution().letterCombinations("2345"))


if __name__ == "__main__":
    main()
