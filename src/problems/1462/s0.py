from typing import List


class Solution:
    def checkIfPrerequisite(
        self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]
    ) -> List[bool]:
        children: List[List[int] | None] = [None] * numCourses
        deps_count = [0] * numCourses

        for dep in prerequisites:
            b, a = dep
            deps_count[a] += 1

            childrenb = children[b]
            if childrenb == None:
                children[b] = [a]
            else:
                childrenb.append(a)

        p2d = [[False for j in range(numCourses)] for k in range(numCourses)]
        for i, count in enumerate(deps_count):
            if count == 0:
                prereq(i, children, deps_count, set(), p2d)

        res = [False] * len(queries)
        for i, query in enumerate(queries):
            if p2d[query[1]][query[0]]:
                res[i] = True

        return res


def prereq(
    c: int,
    children: List[List[int] | None],
    deps_count: List[int],
    cur_pre: set[int],
    p2d: List[List[bool]],
):
    children_c = children[c]
    if children_c != None:
        cur_pre.add(c)
        for child in children_c:
            for item in cur_pre:
                p2d[child][item] = True

            deps_count[child] -= 1
            # if deps_count[child] == 0:
                
            prereq(child, children, deps_count, cur_pre, p2d)
        cur_pre.remove(c)
    return p2d


#
#
#
inputs = [
    # (2, [[1, 0]], [[0, 1], [1, 0]]),
    # (2, [], [[1, 0], [0, 1]]),
    # (5, [[0, 1], [1, 2], [2, 3], [3, 4]], [[0, 4], [4, 0], [1, 3], [3, 0]]),
    (
        10,
        [
            # [3, 9],
            # [3, 2],
            # [3, 7],
            [9, 5],
            # [9, 0],
            # [9, 6],
            [8, 0],
            # [8, 1],
            # [8, 7],
            [5, 0],
            # [5, 2],
            # [5, 1],
            # [5, 7],
            # [5, 6],
            [0, 2],
            # [0, 1],
            # [0, 6],
            # [2, 1],
            # [2, 6],
            # [4, 1],
            # [1, 7],
            # [1, 6],
            # [7, 6],
        ],
        [
            [8, 2],
        ],
    ),
]

for input in inputs:
    print(Solution().checkIfPrerequisite(input[0], input[1], input[2]))
