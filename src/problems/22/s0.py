from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        return gen(n)


def gen(n: int) -> List[str]:
    if n == 1:
        return ["()"]
    elif n == 2:
        return ["(())", "()()"]
    else:
        n_1 = gen(n - 1)

        res = []
        res.extend(map(lambda x: "(" + x + ")", n_1))
        res.extend(map(lambda x: "()" + x, n_1))

        n_h = (n - 1) // 2
        for i in range(n_h):
            i_2 = i + 1
            i_3 = n - 2 - i
            if i_2 == i_3:
                n_2 = gen(i + 1)
                for el2 in n_2:
                    for el3 in n_2:
                        res.append("(" + el2 + ")" + el3)
            else:
                n_2 = gen(i + 1)
                n_3 = gen(n - 2 - i)
                for el2 in n_2:
                    for el3 in n_3:
                        res.append("(" + el2 + ")" + el3)
                        res.append("(" + el3 + ")" + el2)
        return res


def main():
    # print(Solution().generateParenthesis(1))
    # print(Solution().generateParenthesis(2))
    # print(Solution().generateParenthesis(3))
    # print(Solution().generateParenthesis(4))
    print(Solution().generateParenthesis(5))
    print(Solution().generateParenthesis(6))
    print(Solution().generateParenthesis(7))
    print(Solution().generateParenthesis(8))


if __name__ == "__main__":
    main()
