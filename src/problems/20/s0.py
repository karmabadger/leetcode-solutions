class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []
        for c in s:
            if c in "([{":
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                if match_paren(stack.pop()) != c:
                    return False

        return len(stack) == 0


def match_paren(c: str):
    match c:
        case "(":
            return ")"
        case "[":
            return "]"
        case "{":
            return "}"


def main():
    s = Solution()
    print(s.isValid("()"))
    print(s.isValid("()[]{}"))
    print(s.isValid("(]"))
    print(s.isValid("([)]"))
    print(s.isValid("{[]}"))


if __name__ == "__main__":
    main()
