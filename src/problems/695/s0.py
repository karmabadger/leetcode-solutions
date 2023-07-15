from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = [[False] * len(grid[0]) for x in range(len(grid))]

        max_size = 0
        for i, row in enumerate(grid):
            for j, item in enumerate(row):
                if item == 1 and not visited[i][j]:
                    res = area(i, j, grid, visited)
                    if res > max_size:
                        max_size = res

        return max_size


def area(
    r: int,
    c: int,
    grid: List[List[int]],
    visited: List[List[bool]],
) -> int:
    visited[r][c] = True
    res = 1
    # check up
    c1 = c - 1
    if c1 >= 0 and grid[r][c1] == 1 and not visited[r][c1]:
        res += area(r, c - 1, grid, visited)
    # check down
    c1 = c + 1
    if c1 < len(grid[0]) and grid[r][c1] == 1 and not visited[r][c1]:
        res += area(r, c1, grid, visited)

    # check left
    c1 = r - 1
    if c1 >= 0 and grid[c1][c] == 1 and not visited[c1][c]:
        res += area(c1, c, grid, visited)

    # check right
    c1 = r + 1
    if c1 < len(grid) and grid[c1][c] == 1 and not visited[c1][c]:
        res += area(c1, c, grid, visited)

    return res


def print_board(board: List[List[int]]):
    for row in board:
        row_str: List[str] = []
        for item in row:
            row_str.append(str(item))
        print(" | ".join(row_str))
        print(
            "--------------------------------------------------------------------------",
        )


data = [
    ([[0, 1], [1, 1]], 3),
    # ([[1, 1], [1, 1]], 4),
    # (
    #     [
    #         [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    #         [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    #         [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
    #         [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    #     ],
    #     6,
    # ),
    # ([[0, 0, 0, 0, 0, 0, 0, 0]], 0),
]

solution = Solution()
for input, output in data:
    print_board(input)
    print(solution.maxAreaOfIsland(input), output)
