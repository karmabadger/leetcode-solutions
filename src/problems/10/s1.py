from typing import List


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        parsed_p = parse_p(p)
        board: List[List[int]] = [[0] * len(parsed_p) for _ in s]
        res = isMatch(s, parsed_p, 0, 0, board)
        print_2d(board)
        return isMatch(s, parsed_p, 0, 0, board)


def isMatch(s: str, p: List[str], si: int, pi: int, board: List[List[int]]) -> bool:
    if si == len(s) and pi == len(p):
        return True

    if pi >= len(p):
        return False

    if si >= len(s):
        # check if all remaining p are *
        for pi2 in range(pi, len(p)):
            if len(p[pi2]) < 2:
                return False
        return True

    cached = board[si][pi]
    if cached != 0:
        return True if cached == 1 else False

    if len(p[pi]) == 2:
        if p[pi] == ".*":
            # match 0 time to end of string
            for i in range(si, len(s) + 1):
                if isMatch(s, p, i, pi + 1, board):
                    board[si][pi] = 1
                    return True

            board[si][pi] = -1
            return False
        else:
            if isMatch(s, p, si, pi + 1, board):
                board[si][pi] = 1
                return True
            # match 0 time to end of string
            for i in range(si, len(s)):
                if s[i] == p[pi][0]:
                    if isMatch(s, p, i + 1, pi + 1, board):
                        board[si][pi] = 1
                        return True
                else:
                    res = isMatch(s, p, i, pi + 1, board)
                    board[si][pi] = 1 if res else -1
                    return res
            return False
    else:
        if p[pi] == "." or p[pi] == s[si]:
            res = isMatch(s, p, si + 1, pi + 1, board)
            board[si][pi] = 1 if res else -1
            return res
        else:
            board[si][pi] = -1
            return False


def parse_p(p: str) -> List[str]:
    i = 0
    res: List[str] = []
    if len(p) == 0:
        return res
    while i < len(p):
        # peak next
        if i + 1 < len(p) and p[i + 1] == "*":
            cur = p[i : i + 2]
            if len(res) == 0 or cur != res[len(res) - 1]:
                res.append(cur)
            i += 2
        else:
            res.append(p[i])
            i += 1
    return res


def print_2d(board: List[List[int]]):
    for row in board:
        res = []
        for item in row:
            res.append(str(item))
            res.append(" | ")
        res_str = "".join(res)
        print(res_str)
        print("".join(["-"] * len(res_str)))


data = [
    # (("aa", "a"), False),
    # (("aa", "a*"), True),
    # (("ab", ".*"), True),
    # (("ab", "a*b"), True),
    # (("aab", "c*a*b"), True),
    # (("ab", ".*c"), False),
    # (("a", "ab*a"), False),
    # (("bbba", ".*b"), False),
    # (("ababababababababb", "a*b*a*b*a*b*a*b*a*b*a*b*a*b*a*b*b"), True),
    (("acb", "a*.*b*.*a*aa*a*"), True),
]

for input, output in data:
    print(Solution().isMatch(input[0], input[1]), output)
