class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) == 0:
            return True
        elif len(s) % 2 == 1:
            return False
        else:
            if check_valid(s):
                return True
            else:
                


def check_valid(s: str) -> bool:
    count = 0
    for c in s:
        if c == "(":
            count += 1
        else:
            count -= 1
    if count == 0:
        return True
    return False


def main():
    print(Solution().canBeValid("))()))", "010100"))
    print(Solution().canBeValid("()()", "0000"))
    print(Solution().canBeValid(")", "0"))
    # print(Solution().canBeValid("((()))())", "1010010"))


if __name__ == "__main__":
    main()
