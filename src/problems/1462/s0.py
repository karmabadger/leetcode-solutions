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

        reachable = [[False] * numCourses for k in range(numCourses)]
        for i, count in enumerate(deps_count):
            if count == 0:
                reachable_color(i, children, [], reachable)

        return [reachable[q2][q1] for q1, q2 in queries]


def reachable_color(
    c: int,
    children: List[List[int] | None],
    stack: List[int],
    reachable: list[list[bool]],
):
    all_done = True
    reachable_c = reachable[c]
    for parent in stack:
        if not reachable_c[parent]:
            all_done = False
            reachable_c[parent] = True

    if len(stack) == 0 or not all_done:
        children_c = children[c]
        if children_c != None:
            stack.append(c)
            for child in children_c:
                reachable_color(child, children, stack, reachable)
            stack.pop()


inputs = [
    (2, [[1, 0]], [[0, 1], [1, 0]]),
    (2, [], [[1, 0], [0, 1]]),
    (3, [[1, 2], [1, 0], [2, 0]], [[1, 0], [1, 2]]),
    (5, [[0, 1], [1, 2], [2, 3], [3, 4]], [[0, 4], [4, 0], [1, 3], [3, 0]]),
]

for input in inputs:
    print(Solution().checkIfPrerequisite(input[0], input[1], input[2]))
