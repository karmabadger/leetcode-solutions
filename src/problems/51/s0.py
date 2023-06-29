from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        return solveNQueensRecursive(n, 0, [], [])


def solveNQueensRecursive(
    n: int, row_index: int, cols_used: List[int], acc: List[List[str]]
) -> List[List[str]]:
    if n == row_index:
        res = []
        for col in cols_used:
            res.append("".join(["Q" if i == col else "." for i in range(n)]))

        acc.append(res)
        return acc

    for i in range(n):
        if check_valid(cols_used, i):
            cols_used.append(i)
            res = solveNQueensRecursive(n, row_index + 1, cols_used, acc)
            cols_used.pop()

    return acc


def check_valid(cols_used: List[int], next_col) -> bool:
    next_row = len(cols_used)
    for i, col in enumerate(cols_used):
        if col == next_col:
            return False

        # check diagonals
        if abs(next_row - i) == abs(next_col - col):
            return False

    return True


def main():
    print(Solution().solveNQueens(4))
    print(Solution().solveNQueens(1))
    print(Solution().solveNQueens(2))
    print(Solution().solveNQueens(3))


if __name__ == "__main__":
    main()
