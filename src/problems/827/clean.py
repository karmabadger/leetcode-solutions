from typing import List, Tuple, Dict


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        visited = [[False] * len(grid[0]) for x in range(len(grid))]

        p_to_island = {}
        max_res = 0
        for i, row in enumerate(grid):
            for j, item in enumerate(row):
                if item == 1 and not visited[i][j]:
                    res = Island()
                    area(i, j, grid, visited, p_to_island, res)
                    if res.size > max_res:
                        max_res = res.size

        for i, row in enumerate(grid):
            for j, item in enumerate(row):
                if item == 0:
                    res = updated_area(i, j, grid, p_to_island)
                    if res > max_res:
                        max_res = res

        return max_res


class Island:
    def __init__(self) -> None:
        self.size = 0

    def inc(self):
        self.size += 1


def area(
    r: int,
    c: int,
    grid: List[List[int]],
    visited: List[List[bool]],
    p_to_island: Dict[Tuple[int, int], Island],
    island: Island,
):
    visited[r][c] = True
    island.inc()
    p_to_island[(r, c)] = island

    # check up
    c1 = c - 1
    if c1 >= 0 and grid[r][c1] == 1 and not visited[r][c1]:
        area(r, c - 1, grid, visited, p_to_island, island)
    # check down
    c1 = c + 1
    if c1 < len(grid[0]) and grid[r][c1] == 1 and not visited[r][c1]:
        area(r, c1, grid, visited, p_to_island, island)

    # check left
    c1 = r - 1
    if c1 >= 0 and grid[c1][c] == 1 and not visited[c1][c]:
        area(c1, c, grid, visited, p_to_island, island)

    # check right
    c1 = r + 1
    if c1 < len(grid) and grid[c1][c] == 1 and not visited[c1][c]:
        area(c1, c, grid, visited, p_to_island, island)


def updated_area(
    r: int,
    c: int,
    grid: List[List[int]],
    p_to_island: Dict[Tuple[int, int], Island],
) -> int:
    neighbors = []
    res = 1

    r1 = r - 1
    if r1 >= 0:
        c1 = c
        if grid[r1][c1] == 1:
            island = p_to_island[(r1, c1)]
            if not island in neighbors:
                res += island.size
                neighbors.append(island)

    r1 = r + 1
    if r1 < len(grid):
        c1 = c
        if grid[r1][c1] == 1:
            island = p_to_island[(r1, c1)]
            if not island in neighbors:
                res += island.size
                neighbors.append(island)

    c1 = c - 1
    if c1 >= 0:
        r1 = r
        if grid[r1][c1] == 1:
            island = p_to_island[(r1, c1)]
            if not island in neighbors:
                res += island.size
                neighbors.append(island)

    c1 = c + 1
    if c1 < len(grid[0]):
        r1 = r
        if grid[r1][c1] == 1:
            island = p_to_island[(r1, c1)]
            if not island in neighbors:
                res += island.size
                neighbors.append(island)

    return res


def print_board(board: List[List[int]]):
    for row in board:
        row_str: List[str] = []
        for item in row:
            row_str.append(str(item))

        res_str = " | ".join(row_str)
        print(res_str)
        print("".join(["-" for x in range(len(res_str))]))


data = [
    ([[1, 0], [0, 1]], 3),
    ([[1, 1], [1, 0]], 4),
    ([[1, 1], [1, 1]], 4),
    ([[1, 0, 1], [0, 0, 0], [0, 1, 1]], 4),
]

for input, output in data:
    # print_board(input)
    print(Solution().largestIsland(input), output)
