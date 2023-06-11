from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)

        match n:
            case 0:
                return []
            case 1:
                i = ord(digits[0]) - 48
                poss1 = digits_to_letters[i]
                return list(poss1)
            case 2:
                res = []
                for d1 in digits:
                    i = ord(d1) - 48
                    poss1 = digits_to_letters[i]
                    res.append(poss1)

                return gen_list(res, 0, "")
            case 3:
                res = []
                for d1 in digits:
                    i = ord(d1) - 48
                    poss1 = digits_to_letters[i]
                    res.append(poss1)

                return gen_list(res, 0, "")
            case 4:
                res = []
                for d1 in digits:
                    i = ord(d1) - 48
                    poss1 = digits_to_letters[i]
                    res.append(poss1)

                return gen_list(res, 0, "")
            case _:
                return []


def gen_list(arr: List[str], index: int, acc: str) -> List[str]:
    if len(arr) == index:
        return ["".join(acc)]
    else:
        res = []
        for c in arr[index]:
            res.extend(gen_list(arr, index + 1, acc + c))
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
