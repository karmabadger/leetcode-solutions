class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        last_val = matchRoman(s[0])
        cur_val = 0
        for c in s[1:]:
            cur_val = matchRoman(c)
            if cur_val > last_val:
                total -= last_val
            else:
                total += last_val
            last_val = cur_val

        total += last_val
        return total


def matchRoman(s: str) -> int:
    match s:
        case "I":
            return 1
        case "V":
            return 5
        case "X":
            return 10
        case "L":
            return 50
        case "C":
            return 100
        case "D":
            return 500
        case "M":
            return 1000
        case _:
            return 0


# test it out
def main():
    s = Solution()
    print(s.romanToInt("III"))
    print(s.romanToInt("IV"))
    print(s.romanToInt("IX"))
    print(s.romanToInt("LVIII"))
    print(s.romanToInt("MCMXCIV"))


if __name__ == "__main__":
    main()
