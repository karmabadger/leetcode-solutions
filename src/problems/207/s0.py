from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        deps: List[List[int] | None] = [None] * numCourses
        children: List[List[int] | None] = [None] * numCourses

        for dep in prerequisites:
            a, b = dep

            depsa = deps[a]
            if depsa == None:
                deps[a] = [b]
            else:
                depsa.append(b)

            childrenb = children[b]
            if childrenb == None:
                children[b] = [a]
            else:
                childrenb.append(a)

        if not check_has_none(deps):
            return False

        if check_has_self_dep(deps):
            return False

        visited = [False] * numCourses
        for i, dep in enumerate(deps):
            if dep == None:
                if dfs_has_cycle(i, children, visited, []):
                    return False

        for v in visited:
            if not v:
                return False
        return True


def dfs_has_cycle(
    v: int, children: List[List[int] | None], visited: List[bool], back: List[int]
) -> bool:
    visited[v] = True
    childrenv = children[v]
    if childrenv != None:
        back.append(v)
        for child in childrenv:
            if visited[child]:
                if child in back:
                    return True
            else:
                res = dfs_has_cycle(child, children, visited, back)
                if res:
                    return True
        back.pop()

    return False


def check_has_none(deps: List[List[int] | None]) -> bool:
    for dep in deps:
        if dep == None:
            return True
    return False


def check_has_self_dep(deps: List[List[int] | None]) -> bool:
    for i, dep in enumerate(deps):
        if dep != None:
            if i in dep:
                return True
    return False


inputs = [
    # (2, [[1, 0]]),
    # (2, [[1, 0], [0, 1]]),
    # (3, [[1, 0], [2, 1], [0, 2]]),
    # (20, [[0, 10], [3, 18], [5, 5], [6, 11], [11, 14], [13, 1], [15, 1], [17, 4]]),
    (8, [[1, 0], [5, 1], [0, 5]]),
]

for input in inputs:
    print(Solution().canFinish(input[0], input[1]))
