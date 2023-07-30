from typing import List


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return isMatch(s, parse_p(p), 0, 0)


def isMatch(s: str, p: List[str], si: int, pi: int) -> bool:
    if si == len(s) and pi == len(p):
        return True

    if pi >= len(p):
        return False

    if len(p[pi]) == 2:
        if p[pi] == ".*":
            # match 0 time to end of string
            for i in range(si, len(s) + 1):
                if isMatch(s, p, i, pi + 1):
                    return True
            return False
        else:
            if isMatch(s, p, si, pi + 1):
                return True
            # match 0 time to end of string
            for i in range(si, len(s)):
                if s[i] == p[pi][0]:
                    if isMatch(s, p, i + 1, pi + 1):
                        return True
                else:
                    return isMatch(s, p, i, pi + 1)
            return isMatch(s, p, len(s) + 1, pi + 1)
    else:
        if si < len(s):
            return (
                (isMatch(s, p, si + 1, pi + 1))
                if (p[pi] == "." or p[pi] == s[si])
                else False
            )
        else:
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


data = [
    (("aa", "a"), False),
    (("aa", "a*"), True),
    (("ab", ".*"), True),
    (("aab", "c*a*b"), True),
]

for input, output in data:
    print(Solution().isMatch(input[0], input[1]), output)
